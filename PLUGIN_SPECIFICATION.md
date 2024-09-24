# Technical Specification

> **Warning**
This documentation is a template and shall be updated.

## About

This documentation describes the smart contracts and functions supported by the kelp plugin.

#### KELP

| Network | Contract Name | Smart Contract                               |
| ------- | ------------- | -------------------------------------------- |
| Ethereum  | LRTDepositPool    | `0x036676389e48133B63a802f8635AD39E752D375D` |
| Ethereum  | LRTWithdrawalManager    | `0x62de59c08eb5dae4b7e6f7a8cad3006d6965ec16` |


Functions covered by above contract/s :
|Contract | Function | Selector | Displayed Parameters |
| --- | --- | --- | --- |
|LRTDepositPool | depositETH(uint256 minRSETHAmountExpected, string calldata referralId) | `0x72c51c0b`| native_token_amount (eth) |
|LRTDepositPool | depositAsset(address asset, uint256 depositAmount, uint256 minRSETHAmountExpected, string calldata referralId) | `0xc3ae1766`| `asset`, `depositAmount` |
|LRTWithdrawalManager | initiateWithdrawal(address asset, uint256 rsETHUnstaked) | `0xc8393ba9`| `asset`, `rsETHUnstaked` |
|LRTWithdrawalManager | completeWithdrawal(address asset) | `0x6dbaf9ee`| `asset` |
