package com.jd.jim.testframework.executor.config;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.apache.commons.lang3.StringUtils;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class JedisClientConfig {
    private String serverHost;
    private int serverPort;

    public void validate() {
        if (StringUtils.isBlank(serverHost)) {
            throw new IllegalArgumentException("未指定 serverHost");
        }
    }
}
