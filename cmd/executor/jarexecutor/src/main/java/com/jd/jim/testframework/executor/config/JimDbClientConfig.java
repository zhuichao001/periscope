package com.jd.jim.testframework.executor.config;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.apache.commons.lang3.StringUtils;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class JimDbClientConfig {
    public static final String VERSION_NEW = "new";
    public static final String VERSION_OLD = "old";

    private String serviceEndPoint;
    private String jimUrl;
    private String jimDbVersion;

    public void validate() {
        if (StringUtils.isBlank(serviceEndPoint)) {
            throw new IllegalArgumentException("未指定 serviceEndPoint");
        }
        if (StringUtils.isBlank(jimUrl)) {
            throw new IllegalArgumentException("未指定 jimUrl");
        }
        if (StringUtils.isBlank(jimDbVersion) ||
                (!VERSION_NEW.equalsIgnoreCase(jimDbVersion) && !VERSION_OLD.equalsIgnoreCase(jimDbVersion))) {
            throw new IllegalArgumentException("非法 jimDbVersion");
        }
    }
}
