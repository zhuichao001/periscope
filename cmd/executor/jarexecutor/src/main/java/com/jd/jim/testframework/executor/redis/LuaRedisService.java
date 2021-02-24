package com.jd.jim.testframework.executor.redis;

import com.jd.jim.cli.exception.ScriptNotFoundException;
import com.jd.jim.cli.protocol.ScriptOutputType;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-22 18:07
 * Email: wangjinshuai@jd.com
 */
public interface LuaRedisService {

    /**
     * eval
     * @param script
     * @param keys
     * @param args
     * @return
     */
    String eval(String script, List<String> keys, List<String> args);

    /**
     * evalsha
     * @param sha
     * @param keys
     * @param args
     * @return
     * @throws ScriptNotFoundException
     */
    String evalsha(String sha, List<String> keys, List<String> args) throws ScriptNotFoundException;
}
