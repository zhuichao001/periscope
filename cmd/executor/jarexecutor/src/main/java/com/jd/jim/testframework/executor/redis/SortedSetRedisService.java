package com.jd.jim.testframework.executor.redis;

import java.util.Map;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface SortedSetRedisService {

    /**
     * zadd
     * @parma key
     * @param score
     * @param member
     */
    String zadd(String key, double score, String member);

    /**
     * zscore
     * @param key
     * @param member
     * @return
     */
    String zscore(String key, String member);

    /**
     * zincrBy
     * @param key
     * @param delta
     * @param member
     * @return
     */
    String zincrBy(String key, double delta, String member);

    /**
     * zcard
     * @param key
     * @return
     */
    String zcard(String key);

    /**
     * zcount
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zcount(String key, double min, double max);

    /**
     * zrange
     * @param key
     * @param start
     * @param stop
     * @return
     */
    String zrange(String key, long start, long stop);

    /**
     * zrevrange
     * @param key
     * @param start
     * @param stop
     * @return
     */
    String zrevrange(String key, long start, long stop);

    /**
     * zrangebyscore
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zrangeByScore(String key, double min, double max);

    /**
     * zrangebyscore
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zrangeByScore(String key, String min, String max);

    /**
     * zrevrangebyscore
     * @param key
     * @param max
     * @param min
     * @return
     */
    String zrevrangeByScore(String key, double max, double min);

    /**
     * zrevrangebyscore
     * @param key
     * @param max
     * @param min
     * @return
     */
    String zrevrangeByScore(String key, String max, String min);

    /**
     * zrank
     * @param key
     * @param member
     * @return
     */
    String zrank(String key, String member);

    /**
     * zrevrank
     * @param key
     * @param member
     * @return
     */
    String zrevrank(String key, String member);

    /**
     * zrem
     * @param key
     * @param member
     * @return
     */
    String zrem(String key, String... member);

    /**
     * zremrangeByRank
     * @param key
     * @param start
     * @param stop
     * @return
     */
    String zremrangeByRank(String key, long start, long stop);

    /**
     * zremrangeByScore
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zremrangeByScore(String key, double min, double max);

    /**
     * zremrangeByScore
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zremrangeByScore(String key, String min, String max);

    /**
     * zrangeByLex
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zrangeByLex(String key, String min, String max);

    /**
     * zlexcount
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zlexcount(String key, String min, String max);

    /**
     * zremrangeByLex
     * @param key
     * @param min
     * @param max
     * @return
     */
    String zremrangeByLex(String key, String min, String max);

    /**
     * zscan
     * @param key
     * @param cursor
     * @param params
     * @return
     */
    String zscan(String key, String cursor, Map<String, String> params);

    /**
     * zunionstore
     * @param destination
     * @param sets
     * @return
     */
    String zunionstore(String destination, String... sets);

    /**
     * zinterstore
     * @param destination
     * @param sets
     * @return
     */
    String zinterstore(String destination, String... sets);
}
