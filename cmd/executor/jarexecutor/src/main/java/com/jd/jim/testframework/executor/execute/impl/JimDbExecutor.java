package com.jd.jim.testframework.executor.execute.impl;

import com.jd.jim.testframework.executor.redis.RedisService;
import com.jd.jim.testframework.executor.redis.impl.JimkvSdkService;
import lombok.Data;
import lombok.extern.slf4j.Slf4j;

@Slf4j
@Data
public class JimDbExecutor extends BaseExecutor{
    private final JimkvSdkService jimkvSdkService;

    @Override
    public RedisService getRedisService() {
        return jimkvSdkService;
    }
}
