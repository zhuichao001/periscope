package com.jd.jim.testframework.executor.handle.set;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import com.jd.jim.testframework.executor.utils.CustomHelper;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

/**
 * Description:
 * Author: wangjinshuai
 * Date: 2020-12-15 15:52
 * Email: wangjinshuai@jd.com
 */
@Slf4j
@Service
public class SscanHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 2) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);
        String cursor = commandList.get(1);
        Map<String, String> params = CustomHelper.commandList2Map(
                commandList.subList(2, commandList.size()));


        return redisService.getSetRedisService().sscan(key, cursor, params);
    }
}
