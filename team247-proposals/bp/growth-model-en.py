# -*- coding: utf-8 -*-
from pathlib import Path
import json,csv
root=Path(__file__).resolve().parent
rows=[]
for active,fixed,seed in [(1000,3000,1000),(10000,8000,5000),(100000,30000,30000)]:
 for mode,first,renew,cost in [('CNY 1/month',1,1,.4),('CNY 10/month',10,10,2),('First month 1, then 10',1,10,2)]:
  paid=round(active*.2);free=active-paid;referred=round(paid*.7)
  gross=paid*first;fees=gross*.04;service=paid*cost+free*.1;reward=referred*1
  contribution=gross-fees-service-reward
  # Initial cohort only, 70% month-to-month paid retention. Existing free users capped to 1 free trial month.
  retention=.7;paidmonths=paid*(1+retention+retention**2)
  gross90=paid*first+paid*(retention+retention**2)*renew
  cost90=paidmonths*cost+free*.1
  contribution90=gross90*.96-cost90-reward
  rows.append(dict(active_target=active,model=mode,pay_rate=.2,payers=paid,free_users=free,referred_fraction=.7,referred_payers=referred,first_price=first,renewal_price=renew,paid_month_unit_cost=cost,free_trial_unit_cost=.1,fee_rate=.01,refund_reserve_rate=.03,one_time_reward=1,first_month_revenue=gross,first_month_reward=reward,first_month_fees_refund=round(fees,2),first_month_service_cost=round(service,2),first_month_contribution=round(contribution,2),monthly_fixed_economic=fixed,seed_acquisition_cash=seed,first_month_economic_result=round(contribution-fixed-seed,2),retention_monthly=retention,cohort_90d_revenue=round(gross90,2),cohort_90d_service=round(cost90,2),cohort_90d_reward=reward,cohort_90d_contribution=round(contribution90,2),cohort_90d_economic_result_before_build=round(contribution90-3*fixed-seed,2),cohort_90d_paid_months=round(paidmonths,2)))
viral=[]
for name,share,invites,activation,pay in [('Conservative',.3,3,.4,.2),('Neutral',.5,5,.5,.3),('Replacement condition',1,5,.5,.4),('Growth experiment',.7,8,.6,.4)]:
 k=share*invites*activation*pay
 viral.append(dict(scenario=name,share_rate=share,unique_invites_per_sharer=invites,invite_activation_rate=activation,activated_pay_rate=pay,k=round(k,4)))
meta={'date':'2026-11-09','currency':'CNY','status':'All inputs are planning assumptions, not actual traction or provider quotes','target_definition':'Cumulative independently deduplicated activated users; financial stage tables use a hypothetical single newly activated cohort, not existing installed base','reward_interpretation':'One CNY for the first settled payment of a real new paying user to their direct inviter once; no recurring reward in baseline','paid_conversion':.2,'monthly_paid_retention':.7,'free_scope':'Free activated users incur one capped trial month; recurring free usage, reactivation and new cohorts require additional cost','cost_scope':'Monthly fixed economic cost includes operational labor; build cost and unknown taxes, distribution commission, legal/release expenses excluded pending team choice','no_rollup':'The three size stages are alternative cohort experiments; never sum them as one quarter forecast','fixed_costs':'3000/8000/30000 CNY per month are planning placeholders, not confirmed team costs','payment':'1 percent processing plus 3 percent refund reserve is a scenario, not a quote; include separate app-store channel stress before launch'}
(root/'personal-ai-growth-model.json').write_text(json.dumps({'meta':meta,'stages':rows,'referral_scenarios':viral},ensure_ascii=False,indent=2))
with (root/'personal-ai-growth-model.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=rows[0].keys(),lineterminator="\n");w.writeheader();w.writerows(rows)
for r in rows:print(r['active_target'],r['model'],r['first_month_revenue'],r['first_month_economic_result'],r['cohort_90d_economic_result_before_build'])
print('viral',viral)
