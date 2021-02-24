package com.jd.jim.testframework.executor.autoconfig;

import com.jd.jim.testframework.executor.config.JedisClientConfig;
import com.jd.jim.testframework.executor.config.JimDbClientConfig;
import com.jd.jim.testframework.executor.execute.CommandExecutor;
import com.jd.jim.testframework.executor.execute.ExecutorFactory;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;

import java.util.HashMap;
import java.util.Map;

@Slf4j
@Configuration
public class ExecutorConfig {
    private static final int JIMDB_CLIENT = 1;
    private static final int REDIS_CLIENT = 2;

    @Autowired
    Environment environment;

    /**
     * 解析配置文件，生成对应的 CommandExecutor
     * @param prefix 配置项前缀
     * @return
     */
    public CommandExecutor getExecutorByConfig(String prefix) {
        int clientType = environment.getProperty(concatConfigKey(prefix, "clientType"), Integer.class);

        if (clientType == REDIS_CLIENT) {
            // JedisExecutor
            JedisClientConfig jedisClientConfig = getJedisClientConfig(prefix);
            CommandExecutor jedisExecutor = ExecutorFactory.getFactory().newJedisExecutor(jedisClientConfig);

            log.info("====== Create [{}] JedisExecutor with jedisClientConfig: {} ======", prefix, jedisClientConfig);
            return jedisExecutor;
        } else if (clientType == JIMDB_CLIENT) {
            String jimDbVersion = environment.getProperty(concatConfigKey(prefix, "jimDbVersion"));
            Boolean withDrc = environment.getProperty(concatConfigKey(prefix, "withDrc"), Boolean.class);

            if (withDrc != null && withDrc) {
                // JimDbDrcExecutor
                JimDbClientConfig writeJimDbClientConfig =
                        getJimDbClientConfig(concatConfigKey(prefix, "write"), jimDbVersion);

                JimDbClientConfig readJimDbClientConfig =
                        getJimDbClientConfig(concatConfigKey(prefix, "read"), jimDbVersion);

                Map<String, JimDbClientConfig> probeJimDbClientConfigMap = new HashMap<>();
                probeJimDbClientConfigMap.put("write", writeJimDbClientConfig);
                probeJimDbClientConfigMap.put("read", readJimDbClientConfig);
                CommandExecutor jimDbDrcExecutor = ExecutorFactory.getFactory().newDrcExecutor(probeJimDbClientConfigMap);

                log.info("====== Create [{}] DrcExecutor with producerExecutorConfig: {}, consumerExecutorConfig: {} ======"
                        , prefix, writeJimDbClientConfig, readJimDbClientConfig);
                return jimDbDrcExecutor;
            } else {
                // JimDbExecutor
                JimDbClientConfig jimDbClientConfig = getJimDbClientConfig(prefix, jimDbVersion);
                CommandExecutor jimDbExecutor = ExecutorFactory.getFactory().newJimDbExecutor(jimDbClientConfig);
                log.info("====== Create [{}] JimDbExecutor with jimDbClientConfig: {} ======", prefix, jimDbClientConfig);
                return jimDbExecutor;
            }
        }

        throw new IllegalArgumentException("配置文件不正确");
    }

    private JedisClientConfig getJedisClientConfig(String prefix) {
        String clusterHost = environment.getProperty(concatConfigKey(prefix, "clusterHost"));
        int clusterPort = environment.getProperty(concatConfigKey(prefix, "clusterPort"), Integer.class);
        JedisClientConfig jedisClientConfig = new JedisClientConfig(clusterHost, clusterPort);
        jedisClientConfig.validate();
        return jedisClientConfig;
    }

    private JimDbClientConfig getJimDbClientConfig(String prefix, String jimDbVersion) {
        String serviceEndpoint = environment.getProperty(concatConfigKey(prefix, "serviceEndpoint"));
        String jimUrl = environment.getProperty(concatConfigKey(prefix, "jimUrl"));
        JimDbClientConfig jimDbClientConfig = new JimDbClientConfig(serviceEndpoint, jimUrl, jimDbVersion);
        jimDbClientConfig.validate();
        return jimDbClientConfig;

    }

    private String concatConfigKey(String prefix, String configKey) {
        return prefix + "." + configKey;
    }

}
