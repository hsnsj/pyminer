# 数据集信息


本数据集包含2005年4月至2005年9月台湾信用卡客户的逾期、个人信息、信用数据、付款历史及账单信息。

**你应该通过 config.csv 指定变量类型**

约定:

连续变量: is_tobe_bin=1 且 is_candidate=1

离散变量: is_tobe_bin=0 且 is_candidate=1

## 内容


本数据集包含25个变量:

 - ID: 每个客户的ID
 - LIMIT_BAL:授信金额（新台币，含个人及家庭/补充授信）
 - SEX: 性别 (1=男, 2=女)
 - EDUCATION: (1=研究生, 2=本科, 3=高中, 4=其他, 5=未知, 6=未知)
 - MARRIAGE: 婚姻状态 (1=已婚, 2=单身, 3=其他)
 - AGE: 年龄
 - PAY_0: 2005年9月还款状态 (-1=正常支付, 1=付款延迟1个月, 2=付款延迟2个月, ... 8=付款延迟8个月, 9=付款延迟9个月及以上)
 - PAY_2: 2005年8月还款状态 (单位同上)
 - PAY_3: 2005年7月还款状态 (单位同上)
 - PAY_4: 2005年6月还款状态 (单位同上)
 - PAY_5: 2005年5月还款状态 (单位同上)
 - PAY_6: 2005年4月还款状态 (单位同上)
 - BILL_AMT1: 2005年9月的账单金额 (新台币)
 - BILL_AMT2: 2005年8月的账单金额 (新台币)
 - BILL_AMT3: 2005年7月的账单金额 (新台币)
 - BILL_AMT4: 2005年6月的账单金额 (新台币)
 - BILL_AMT5: 2005年5月的账单金额 (新台币)
 - BILL_AMT6: 2005年4月的账单金额 (新台币)
 - PAY_AMT1: 2005年9月的提前还款金额 (新台币)
 - PAY_AMT2: 2005年8月的提前还款金额 (新台币)
 - PAY_AMT3: 2005年7月的提前还款金额 (新台币)
 - PAY_AMT4: 2005年6月的提前还款金额 (新台币)
 - PAY_AMT5: 2005年5月的提前还款金额 (新台币)
 - PAY_AMT6: 2005年4月的提前还款金额 (新台币)
 - target: 是否逾期 (1=是, 0=否)
