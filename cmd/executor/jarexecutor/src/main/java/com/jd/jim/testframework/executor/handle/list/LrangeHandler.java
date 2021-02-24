package com.jd.jim.testframework.executor.handle.list;

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
@Service(value = "lrangeHandler")
public class LrangeHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 3) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        return redisService.getListRedisService().lRange(commandList.get(0), Long.valueOf(commandList.get(1)), Long.valueOf(commandList.get(2)));
    }
}
