﻿RP/0/0/CPU0:XR-P1#sh running-config 
Tue Nov 28 12:59:09.708 UTC
Building configuration...
!! IOS XR Configuration 6.0.1
!! Last configuration change at Tue Nov 28 10:25:18 2017 by cisco
!
hostname XR-P1
ipv4 unnumbered mpls traffic-eng Loopback0
interface Loopback0
 ipv4 address 100.64.1.1 255.255.255.255
!
interface MgmtEth0/0/CPU0/0
 shutdown
!
interface GigabitEthernet0/0/0/0.12
 ipv4 address 169.254.12.1 255.255.255.0
 encapsulation dot1q 12
!
interface GigabitEthernet0/0/0/0.13
 ipv4 address 169.254.13.1 255.255.255.0
 encapsulation dot1q 13
!
interface GigabitEthernet0/0/0/0.14
 ipv4 address 169.254.14.1 255.255.255.0
 encapsulation dot1q 14
!
interface GigabitEthernet0/0/0/0.16
 ipv4 address 169.254.16.1 255.255.255.0
 encapsulation dot1q 16
!
interface GigabitEthernet0/0/0/0.111
 ipv4 address 169.254.111.11 255.255.255.0
 encapsulation dot1q 111
!
interface GigabitEthernet0/0/0/0.112
 ipv4 address 169.254.112.1 255.255.255.0
 encapsulation dot1q 112
!
interface GigabitEthernet0/0/0/1
 shutdown
!
interface GigabitEthernet0/0/0/2
 shutdown
!
router isis fuck
 is-type level-2-only
 net 49.0001.0000.0001.00
 log adjacency changes
 address-family ipv4 unicast
  metric-style wide
  mpls traffic-eng level-2-only
  mpls traffic-eng router-id Loopback0
  segment-routing mpls
 !
 interface Loopback0
  address-family ipv4 unicast
   prefix-sid index 1
  !
 !
 interface GigabitEthernet0/0/0/0.12
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.13
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.14
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.16
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.111
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
 interface GigabitEthernet0/0/0/0.112
  point-to-point
  address-family ipv4 unicast
   fast-reroute per-prefix
   fast-reroute per-prefix ti-lfa
  !
 !
!
mpls oam
!
mpls traffic-eng
 pce
  peer source ipv4 100.64.1.1
  peer ipv4 150.1.255.253
  !
  segment-routing
  logging events peer-status
  stateful-client
   instantiation
  !
 !
 auto-tunnel pcc
  tunnel-id min 1 max 99
 !
 reoptimize timers delay installation 0
!
segment-routing
!
end

