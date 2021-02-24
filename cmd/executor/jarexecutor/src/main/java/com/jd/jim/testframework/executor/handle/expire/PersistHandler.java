package com.jd.jim.testframework.executor.handle.expire;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
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
@Service(value = "persistHandler")
public class PersistHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (CollectionUtils.isEmpty(commandList)) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        return redisService.getExpireRedisService().persist(commandList.get(0));
    }
}
