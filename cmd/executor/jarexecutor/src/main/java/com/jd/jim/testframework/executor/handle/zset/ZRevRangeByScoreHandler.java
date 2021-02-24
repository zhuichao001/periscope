package com.jd.jim.testframework.executor.handle.zset;

import com.jd.jim.testframework.executor.constant.CommonConstant;
import com.jd.jim.testframework.executor.exception.InvalidParamException;
import com.jd.jim.testframework.executor.handle.BaseHandler;
import lombok.extern.slf4j.Slf4j;
import org.apache.commons.collections4.CollectionUtils;
import org.apache.commons.lang3.StringUtils;
import org.springframework.stereotype.Service;

import java.util.List;

@Slf4j
@Service(value = "zRevRangeByScoreHandler")
public class ZRevRangeByScoreHandler extends BaseHandler {

    @Override
    public String handle(List<String> commandList) {
        if (CollectionUtils.isEmpty(commandList) || commandList.size() < 3) {
            throw new InvalidParamException(CommonConstant.INVALID_PARAM);
        }

        String key = commandList.get(0);
        String maxStr = commandList.get(1);
        String minStr = commandList.get(2);

        if (StringUtils.isNumeric(minStr) && StringUtils.isNumeric(maxStr)) {
            double min = Double.parseDouble(minStr);
            double max = Double.parseDouble(maxStr);
            return redisService.getSortedSetRedisService().zrevrangeByScore(key, max, min);
        } else {
            return redisService.getSortedSetRedisService().zrevrangeByScore(key, maxStr, minStr);
        }
    }

}
