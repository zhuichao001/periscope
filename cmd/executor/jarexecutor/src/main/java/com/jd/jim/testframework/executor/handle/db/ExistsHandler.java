package com.jd.jim.testframework.executor.handle.db;

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
@Service(value = "existsHandler")
public class ExistsHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (CollectionUtils.isEmpty(commandList)) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        return redisService.getDbRedisService().exists(commandList.get(0));
    }
}
