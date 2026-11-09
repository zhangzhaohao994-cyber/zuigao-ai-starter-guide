# -*- coding: utf-8 -*-
from pathlib import Path
import json,math,csv
MODELS=[]
def row(pid,case,n,revenue,costs,**kw):
 total=round(sum(costs.values()),2);d=dict(project=pid,scenario=case,paid_customers=n,revenue=revenue,costs=costs,total_cost=total,target_surplus=round(revenue-total,2),**kw);MODELS.append(d);return d
for case,n,fixed in [('保守',30000,26000),('目标',100000,26000),('冲刺',200000,26000),('百万阶段',1000000,120000),('千万阶段',10000000,1000000)]:
 row('persona',case,n,n,{'build_and_operations':fixed,'service_allowance':n*.1,'payment_tax_refund_reserve':n*.04,'seed_and_content_marketing':n*.05,'capped_referral_pool':n*.05},unit_contribution=.76,break_even=math.ceil(fixed/.76),period='90-day launch target' if n<=200000 else 'later-stage standalone capacity illustration')
for case,n,sub,marketing,fixed in [('保守',4,2,20000,18000),('目标',12,8,36000,18000),('冲刺',20,16,60000,24000)]:
 row('industry',case,n,n*19800+sub*6800,{'implementation_delivery':n*4800,'subscription_delivery':sub*1800,'payment_tax_refund_reserve':(n*19800+sub*6800)*.08,'sales_marketing':marketing,'build':40000,'operations':fixed},subscription_customer_months=sub,period='90 days after resource approval')
for case,n,marketing,free,fixed in [('保守',200,20000,1000,15000),('目标',1000,40000,2000,15000),('冲刺',3000,100000,6000,30000)]:
 row('story',case,n,n*299,{'paid_work_delivery':n*80,'payment_tax_refund_reserve':n*299*.08,'marketing':marketing,'free_samples':free,'build':30000,'operations':fixed},standard_orders=int(n*.8),premium_orders=int(n*.2),period='90-day selling and delivery window')

Path("economics-v7.json").write_text(json.dumps({"currency":"CNY","basis":"Unvalidated operating targets","scenarios":MODELS},ensure_ascii=False,indent=2))
for r in MODELS:
 assert abs(r["revenue"]-sum(r["costs"].values())-r["target_surplus"])<.001
 print(r["project"],r["scenario"],r["revenue"],r["total_cost"],r["target_surplus"])
