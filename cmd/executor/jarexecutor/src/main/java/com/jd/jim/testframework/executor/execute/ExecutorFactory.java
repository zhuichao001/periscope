package com.jd.jim.testframework.executor.execute;

import com.jd.jim.cli.Cluster;
import com.jd.jim.cli.ReloadableJimClientFactory;
import com.jd.jim.cli.config.ConfigLongPollingClientFactory;
import com.jd.jim.testframework.executor.config.JedisClientConfig;
import com.jd.jim.testframework.executor.config.JimDbClientConfig;
import com.jd.jim.testframework.executor.execute.impl.JedisExecutor;
import com.jd.jim.testframework.executor.execute.impl.JimDbExecutor;
import com.jd.jim.testframework.executor.execute.impl.DrcExecutor;
import com.jd.jim.testframework.executor.redis.impl.JedisService;
import com.jd.jim.testframework.executor.redis.impl.JimkvSdkService;
import io.jimdb.JimdbNewConfigClientFactory;
import io.jimdb.ReloadableJimdbNewClientFactory;
import lombok.extern.slf4j.Slf4j;
import redis.clients.jedis.Jedis;

import java.util.Map;

@Slf4j
public class ExecutorFactory {
    private static final ExecutorFactory instance = new ExecutorFactory();

    public static ExecutorFactory getFactory() {
        return instance;
    }

    private ExecutorFactory() {}

    public JedisExecutor newJedisExecutor(JedisClientConfig jedisClientConfig) {
        Jedis jedis = new Jedis(
                jedisClientConfig.getServerHost(),
                jedisClientConfig.getServerPort());

        return new JedisExecutor(new JedisService(jedis));
    }

    public JimDbExecutor newJimDbExecutor(JimDbClientConfig jimDbClientConfig) {
        String jimDbVersion = jimDbClientConfig.getJimDbVersion();

        if (JimDbClientConfig.VERSION_NEW.equalsIgnoreCase(jimDbVersion)) {
            return newJimDbNewExecutor(jimDbClientConfig);
        } else if (JimDbClientConfig.VERSION_OLD.equalsIgnoreCase(jimDbVersion)) {
            return newJimDbOldExecutor(jimDbClientConfig);
        }

        throw new IllegalArgumentException("jimDbVersion字段值非法: " + jimDbVersion);
    }

    private JimDbExecutor newJimDbOldExecutor(JimDbClientConfig jimDbOldClientConfig) {
        String serviceEndpoint = jimDbOldClientConfig.getServiceEndPoint();
        String jimUrl = jimDbOldClientConfig.getJimUrl();

        ReloadableJimClientFactory factory = createJimDbOldClientFactory(serviceEndpoint, jimUrl);
        Cluster jimDbClient =  factory.getClient();

        return new JimDbExecutor(new JimkvSdkService(jimDbClient));
    }

    private ReloadableJimClientFactory createJimDbOldClientFactory(String serviceEndpoint, String jimUrl) {
        ConfigLongPollingClientFactory configClientFactory = new ConfigLongPollingClientFactory(serviceEndpoint);

        ReloadableJimClientFactory factory = new ReloadableJimClientFactory();
        factory.setJimUrl(jimUrl);
        factory.setIoThreadPoolSize(5);
        factory.setComputationThreadPoolSize(5);
        factory.setRequestQueueSize(100000);
        factory.setConfigClient(configClientFactory.create());

        return factory;
    }

    private JimDbExecutor newJimDbNewExecutor(JimDbClientConfig jimDbNewClientConfig) {
        String serviceEndPoint = jimDbNewClientConfig.getServiceEndPoint();
        String newJimUrl = jimDbNewClientConfig.getJimUrl();

        ReloadableJimdbNewClientFactory jimdbNewClientFactory =
                createJimDbNewClientFactory(serviceEndPoint, newJimUrl);

        Cluster jimDbNewClient = jimdbNewClientFactory.getClient();

        return new JimDbExecutor(new JimkvSdkService(jimDbNewClient));
    }

    private ReloadableJimdbNewClientFactory createJimDbNewClientFactory(String serviceEndPoint, String newJimUrl) {
        JimdbNewConfigClientFactory newConfigClientFactory = new JimdbNewConfigClientFactory();
        // masterURL
        newConfigClientFactory.setServiceEndpoint(serviceEndPoint);
        ReloadableJimdbNewClientFactory newJimdbFactory = new ReloadableJimdbNewClientFactory();
        newJimdbFactory.setRouterManager(newConfigClientFactory.create());
        newJimdbFactory.setJimUrl(newJimUrl);
        // receive data timeout from server , default 2000ms
        newJimdbFactory.setReadTimeout(2000);
        // crate connection timeout from server , default 2000ms
        newJimdbFactory.setConnTimeOut(2000);
        // netty io thread,default 10 ，unless you are proficient in netty, it is not recommended to edit
        // 管理连接的io线程数
        newJimdbFactory.setIoThreadPoolSize(10);
        // netty water mark ,default low water mark 32 * 1024 ,high water mark 64 * 1024(高低水位概念请百度netty)
        newJimdbFactory.setWriteBufferLowWaterMark(32 * 1024);
        newJimdbFactory.setWriteBufferHighWaterMark(64 * 1024);
        //在超时时间内的重试次数
        newJimdbFactory.setRetry(1);

        return newJimdbFactory;
    }

    public DrcExecutor newDrcExecutor(Map<String, JimDbClientConfig> jimDbClientConfigMap) {
        DrcExecutor drcExecutor = new DrcExecutor();

        JimDbClientConfig writeJimDbClientConfig = jimDbClientConfigMap.get("write");
        JimDbExecutor writeExecutor = newJimDbExecutor(writeJimDbClientConfig);
        drcExecutor.setWriteExecutor(writeExecutor);

        JimDbClientConfig readJimDbClientConfig = jimDbClientConfigMap.get("read");
        JimDbExecutor readExecutor = newJimDbExecutor(readJimDbClientConfig);
        drcExecutor.setReadExecutor(readExecutor);

        return drcExecutor;
    }
}