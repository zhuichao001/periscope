package com.jd.jim.testframework.executor.redis;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface DbRedisService {

    /**
     * exists
     * @param key
     * @return
     */
    String exists(String key);

    /**
     * type
     * @param key
     * @return
     */
    String type(String key);

    /**
     * rename
     * @param oldKey
     * @param newKey
     * @return
     */
    String rename(String oldKey, String newKey);

    /**
     * renamenx
     * @param oldKey
     * @param newKey
     * @return
     */
    String renamenx(String oldKey, String newKey);

    /**
     * move
     * @param key
     * @param db
     * @return
     */
    String move(String key, int db);

    /**
     * del
     * @param key
     * @return
     */
    String del(String... key);

    /**
     * randomKey
     * @return
     */
    String randomKey();

    /**
     * dbSize
     * @return
     */
    String dbSize();

    /**
     * keys
     * @return
     */
    String keys(String pattern);

    /**
     * TODO 支持 pattern 与 count
     * hscan
     * @param commandList
     * @return
     */
    String scan(List<String> commandList);

    /**
     * sort
     * @param key
     * @return
     */
    String sort(String key);

    /**
     * flushDB
     * @return
     */
    String flushDB();

    /**
     * flushAll
     * @return
     */
    String flushAll();

    /**
     * select
     * @param index
     * @return
     */
    String select(int index);

    /**
     * swapDB
     * @param index1
     * @param index2
     * @return
     */
    String swapDB(int index1, int index2);


}
