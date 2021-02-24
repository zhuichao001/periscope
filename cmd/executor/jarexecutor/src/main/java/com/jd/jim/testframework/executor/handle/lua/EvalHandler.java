package com.jd.jim.testframework.executor.handle.lua;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:52
 * Email: wangjinshuai@jd.com
 */
@Service
public class EvalHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 2) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String script = commandList.get(0);
        int numKeys = Integer.valueOf(commandList.get(1));

        List<String> keys = new ArrayList<>();
        if (numKeys > 0) {
            keys = commandList.subList(2, 2 + numKeys);
        }

        List<String> args = new ArrayList<>();
        if (commandList.size() > (2 + numKeys)) {
            args = commandList.subList(2 + numKeys, commandList.size());
        }

        return redisService.getLuaRedisService().eval(script, keys, args);
    }
}
