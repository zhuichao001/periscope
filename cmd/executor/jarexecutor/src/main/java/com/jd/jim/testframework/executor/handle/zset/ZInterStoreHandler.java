package com.jd.jim.testframework.executor.handle.zset;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "zInterStoreHandler")
public class ZInterStoreHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 2) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String destination = commandList.get(0);
        String[] sets = commandList.subList(1, commandList.size())
                .toArray(new String[0]);

        return redisService.getSortedSetRedisService().zinterstore(destination, sets);
    }

}
