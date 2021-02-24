package com.jd.jim.testframework.executor.handle.debug;

import com.jd.jim.testframework.executor.handle.BaseHandler;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:52
 * Email: wangjinshuai@jd.com
 */
@Service
public class PingHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (!CollectionUtils.isEmpty(commandList)) {
            String message = commandList.get(0);
            return redisService.getDebugRedisService().ping(message);
        } else {
            return redisService.getDebugRedisService().ping();
        }
    }
}
