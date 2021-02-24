package com.jd.jim.testframework.executor.handle.hyperloglog;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "pfMergeHandler")
public class PfMergeHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {

        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 2) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }
        String destKey = commandList.get(0);
        String[] sourceKey = commandList.subList(1, commandList.size())
                .stream().toArray(String[]::new);

        return redisService.getHyperLogLogRedisService().pfadd(destKey, sourceKey);
    }
}
