package com.jd.jim.testframework.executor.handle.expire;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.concurrent.TimeUnit;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:52
 * Email: wangjinshuai@jd.com
 */
@Slf4j
@Service(value = "expireHandler")
public class ExpireHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 2) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);

        Long expireTime = Long.valueOf(commandList.get(1));

        return redisService.getExpireRedisService().expire(key, expireTime, TimeUnit.SECONDS);
    }
}
