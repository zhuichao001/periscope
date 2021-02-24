package com.jd.jim.testframework.executor.receive;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;

/**
 * Description: 通过 udp 协议接受 上游 测试用例入参
 * Author: wangjinshuai
 * Date: 2020-12-15 11:24
 * Email: wangjinshuai@jd.com
 */
@Slf4j
@Service
public class UdpCommandReceiver implements CommandReceiver {

    private DatagramSocket ds = null;
    private volatile boolean running = false;

    public UdpCommandReceiver() {}

    public UdpCommandReceiver(String udpReceiverHost, int udpReceiverPort) {
        try {
            ds = new DatagramSocket(udpReceiverPort);
            ds.setSoTimeout(2000);
        } catch (Exception e) {
            log.error("UdpReceiver init ds occur error", e);
        }
    }

    @Override
    public void stop() {
        running = false;
    }

    @Override
    public void start() throws IOException {
        log.info("UdpCommandReceiver 启动");
        running = true;

        Thread udpServerThread = new Thread(() -> startUdpServer());
        udpServerThread.setDaemon(true);
        udpServerThread.start();
    }

    private void startUdpServer() {
        byte[] buffer = new byte[1024];
        DatagramPacket packet = new DatagramPacket(buffer, buffer.length);

        while (running) {
            try {
                ds.receive(packet);
                String data = new String(packet.getData(), packet.getOffset(), packet.getLength());
                CommandContainer.getSingleton().putCommand(data);
            } catch (Exception e) {
                log.error("error receive command", e);
            }
        }

        if (null != ds) {
            ds.disconnect();
            log.info("UdpCommandReceiver 关闭");
        }
    }

}