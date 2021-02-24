package com.jd.jim.testframework.executor.execute.impl;

import com.jd.jim.testframework.executor.redis.RedisService;
import com.jd.jim.testframework.executor.redis.impl.JedisService;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Data
public class JedisExecutor extends BaseExecutor {
    private final JedisService jedisService;

    @Override
    public RedisService getRedisService() {
        return jedisService;
    }
}
