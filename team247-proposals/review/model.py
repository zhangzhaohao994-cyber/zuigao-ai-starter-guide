import json,csv,math
from pathlib import Path
out=Path(__file__).parent
rows=[]
for label,leads,reach,meeting,close,cap,cohorts,subs,acq in [
 ('保守',120,.5,.25,.2,3,[1,1,1],[0,0,1],3000),
 ('基准',200,.6,.3,.3,10,[2,4,4],[0,1,3],4000),
 ('乐观',300,.7,.35,.35,15,[3,6,6],[0,2,6],6000)]:
 pilots=min(math.floor(leads*reach*meeting*close),cap)
 assert pilots==sum(cohorts)
 sm=sum(subs);revenue=pilots*2980+sm*1980
 direct=pilots*1380+sm*600+revenue*.04
 sales_labor=60*80
 fixed=32400+3000
 cash=pilots*420+sm*280+revenue*.04+2000+3000+acq
 rows.append(dict(product='industry',scenario=label,qualified_targets=leads,reachable_rate=reach,meeting_rate=meeting,pilot_rate=close,capacity=cap,pilot_cohorts=cohorts,monthly_subscribers=subs,pilots=pilots,subscriber_months=sm,revenue=revenue,direct_cost=round(direct,2),contribution=round(revenue-direct,2),acquisition_cash=acq,acquisition_labor=sales_labor,fixed_economic_cost=fixed,economic_result=round(revenue-direct-acq-sales_labor-fixed,2),cash_outlay=round(cash,2),cash_balance_if_all_collected=round(revenue-cash,2),cash_cac=round(acq/pilots,2),full_cac=round((acq+sales_labor)/pilots,2),ending_mrr=subs[-1]*1980))
for label,visits,activation,pay,retention,acq in [('保守',300,.20,.03,.40,1500),('基准',500,.20,.08,.60,1500),('乐观',800,.25,.15,.75,2500)]:
 active=math.floor(visits*activation);paid=math.floor(active*pay)
 # One initial cohort, three monthly renewals observed over 90 days: expected paid months, not whole customers.
 pm=paid*(1+retention+retention**2)
 revenue=pm*29
 direct=active*2+pm*(7+29*.24)
 fixed=240*150+100*80+3000+3*800
 cash=active*2+pm*(5+29*.24)+3000+3*800+acq
 rows.append(dict(product='persona',scenario=label,qualified_visits=visits,activation_rate=activation,pay_rate=pay,monthly_retention=retention,active=active,initial_payers=paid,expected_paid_months=round(pm,4),revenue=round(revenue,2),direct_cost=round(direct,2),contribution=round(revenue-direct,2),acquisition_cash=acq,acquisition_labor=40*80,fixed_economic_cost=fixed,economic_result=round(revenue-direct-acq-40*80-fixed,2),cash_outlay=round(cash,2),cash_balance_if_all_collected=round(revenue-cash,2),cash_cac=round(acq/paid,2),full_cac=round((acq+40*80)/paid,2),expected_ending_mrr=round(paid*retention**2*29,2)))
for label,visits,activation,pay,repeat,acq in [('保守',400,.15,.05,.10,1200),('基准',500,.20,.12,.25,1200),('乐观',800,.25,.20,.40,2000)]:
 active=math.floor(visits*activation);paid=math.floor(active*pay);orders=paid*(1+repeat)
 revenue=orders*69
 # One free complete short story per activated user; full cost including review.
 direct=active*6+orders*(18+69*.08)
 fixed=140*150+80*80+2000+3*600
 cash=active*4+orders*(10+69*.08)+2000+3*600+acq
 rows.append(dict(product='story',scenario=label,qualified_visits=visits,activation_rate=activation,pay_rate=pay,repeat_rate=repeat,active=active,payers=paid,expected_orders=round(orders,2),revenue=round(revenue,2),direct_cost=round(direct,2),contribution=round(revenue-direct,2),acquisition_cash=acq,acquisition_labor=40*80,fixed_economic_cost=fixed,economic_result=round(revenue-direct-acq-40*80-fixed,2),cash_outlay=round(cash,2),cash_balance_if_all_collected=round(revenue-cash,2),cash_cac=round(acq/paid,2),full_cac=round((acq+40*80)/paid,2)))
meta={'version':'2026-11-09','currency':'CNY','period_days':90,'status':'ALL INPUTS ARE PLANNING ASSUMPTIONS; NOT FORECASTS OR OBSERVED RESULTS','revenue_basis':'Gross delivered contract revenue before modeled refund reserve; taxes excluded pending seller entity confirmation. All cash collections assumed only for scenario arithmetic.','rate_basis':{'engineering_hour':150,'product_delivery_hour':80,'professional_review_hour':150},'limitations':['No confirmed customers, channel reach or sales','Consumer cohorts recruited at day 0 for comparable full 90-day observation; staggered acquisition requires shifting windows','Fixed internal labor counted economically; cash_outlay assumes internal labor not paid incrementally','Payment fees and refund reserves are assumptions, not provider quotes','No tax, actual seller entity, FX, licensing minimum guarantees or statutory release costs priced; blocked until quoted','Costs represent experiments, not full production launches']}
(out/'model.json').write_text(json.dumps({'meta':meta,'scenarios':rows},ensure_ascii=False,indent=2))
keys=list(dict.fromkeys(k for r in rows for k in r))
with (out/'model.csv').open('w',newline='',encoding='utf-8-sig') as f:
 w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
for r in rows:
 print(r['product'],r['scenario'],'revenue',r['revenue'],'contribution',r['contribution'],'economic',r['economic_result'],'cash',r['cash_outlay'])
assert len(rows)==9
