package com.jd.jim.testframework.executor;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class AppStartTests {

	@Test
	void contextLoads() {
		String str = "- SET: 'SET {key} {val}'";

		String[] result = str.split(" ");

		for (String temp : result) {
			System.out.println("1234=" + temp);
		}
	}

}
