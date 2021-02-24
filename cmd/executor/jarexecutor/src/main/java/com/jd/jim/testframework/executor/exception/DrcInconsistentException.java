package com.jd.jim.testframework.executor.exception;

import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
public class DrcInconsistentException extends RuntimeException {

    public DrcInconsistentException(String producerResult, String consumerResult) {
        super(String.format(
                "Drc producer and consumer result inconsistent, producerResult=%s, consumerResult=%s",
                producerResult, consumerResult));
    }
}
