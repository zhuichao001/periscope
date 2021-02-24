package com.jd.jim.testframework.executor.handle.string;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:52
 * Email: wangjinshuai@jd.com
 */
@Slf4j
@Service
public class SetHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList)) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        for (int i = 0; i < commandList.size(); i = i + 2) {
            redisService.getStringRedisService().set(commandList.get(i), commandList.get(i + 1));
        }

        return CommonConstant.OK;
    }
}
