package com.jd.jim.testframework.executor.handle;

import com.jd.jim.testframework.executor.redis.RedisService;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:23
 * Email: wangjinshuai@jd.com
 */
public abstract class BaseHandler {

    protected RedisService redisService;

    /**
     * 执行处理
     * @param commandList
     * @return
     */
    public abstract String handle(List<String> commandList) throws Exception;

    public void setRedisService(RedisService redisService) {
        this.redisService = redisService;
    }
}
