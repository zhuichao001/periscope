package com.jd.jim.testframework.executor.redis;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface HyperLogLogRedisService {

    /**
     * pfadd
     * @parma key
     * @param element
     * @return
     */
    String pfadd(String key, String... element);

    /**
     * pfcount
     * @parma key
     * @return
     */
    String pfcount(String key);

    /**
     * pfmerge
     * @param destkey
     * @param sourcekey
     * @return
     */
    String pfmerge(String destkey, String... sourcekey);

}
