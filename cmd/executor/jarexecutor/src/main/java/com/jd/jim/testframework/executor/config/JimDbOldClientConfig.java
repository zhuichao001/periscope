package com.jd.jim.testframework.executor.config;

import lombok.Data;

/**
 * 若 jimdb 新旧版本配置项有差异时，需将配置放到 JimDbOldClientConfig 和 JimDbNewClientConfig
 */
@Data
public class JimDbOldClientConfig extends JimDbClientConfig {
}
