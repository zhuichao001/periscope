package com.jd.jim.testframework.executor.redis;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface ClientServerRedisService {

    /**
     * auth
     * @param password
     * @return
     */
    String auth(String password);
}
