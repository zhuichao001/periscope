package com.jd.jim.testframework.executor.send;

import lombok.extern.slf4j.Slf4j;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;

/**
 * Description: 测试用例处理结果 以udp协议发送给下游differ
 * Author: wangjinshuai
 * Date: 2020-12-15 11:25
 * Email: wangjinshuai@jd.com
 */
@Slf4j
public class UdpResultSender implements ResultSender {

    private String udpSenderHost;
    private int udpSenderPort;

    public UdpResultSender(String senderHost, int senderPort) {
        this.udpSenderHost = senderHost;
        this.udpSenderPort = senderPort;
    }

    @Override
    public void sendResult(String result) {
        try {
            byte[] sendData = result.getBytes();
            InetAddress remoteAddress = InetAddress.getByName(udpSenderHost);
            DatagramPacket sendPacket =
                    new DatagramPacket(sendData, sendData.length, remoteAddress, udpSenderPort);
            new DatagramSocket().send(sendPacket);
        } catch (Exception e) {
            log.error("UdpSender send occur error", e);
        }
    }
}
