# Team247 | Three business plans — V6

Prepared by 最高. 2026-11-09. All prices, targets and budgets are planning assumptions.


# 01 Personal AI for everyday life


## Page 01 | Executive summary & ambition

The ambition is a useful personal AI assistant for a mass audience. 1,000, 10,000 and 100,000 users are stage targets; reminders are one capability.

### Product ambition
I want to build a personal AI that ordinary people can use over time: understand requests, work with documents, find information, form plans, remember preferences the user chooses to retain, and help complete tasks within authorized limits. Becoming a widely used, everyday application is the long-term ambition, not a claim of an established market position.

| Item | Proposal for discussion |
| --- | --- |
| Audience | People with recurring needs in life, study and work |
| Growth stages | 1,000 → 10,000 → 100,000 genuinely activated users |
| Pricing hypotheses | CNY 1/month; CNY 10/month; or CNY 1 in month one, then 10/month |
| Acquisition concept | A one-time CNY 1 reward to the direct inviter for each genuine new payer's first eligible payment |
| Key evidence | Usefulness, retention, payment, referral coefficient and unit cost |
| Technical position | Capabilities, platform, models, price and investment to be assessed jointly with the team |

**Ten customers or 100 users are early checkpoints, not a ceiling on ambition.** I will drive the product vision, market work and validation. An architecture that has not been discussed is not a team-approved implementation plan.


## Page 02 | Customers & the problem

A broad ambition still needs specific launch use cases that give people a reason to return.

| Initial audience hypothesis | Actual tasks | Value to test |
| --- | --- | --- |
| Students and early-career users | Read material, explain questions, organize plans | Less switching between tools; easier understanding |
| Employees and independent workers | Draft copy, prepare meeting material, manage tasks and find information | Outputs that can be used and developed further |
| Everyday users | Itineraries, lists, questions and personal notes | Voice input, continuity of preferences and records |

### Who pays
The user pays a monthly fee for a real AI service. An invited person must receive independent product value; payment should not primarily buy eligibility to recruit others for rewards.

### Differentiation questions
General-purpose assistants already exist. We need to test whether daily use is simpler, tasks actually get completed, personal settings carry forward, the low price includes enough usable capacity, and people share because the product helps them.

### Initial cohorts
All three groups belong to the long-term market. The first 1,000 should be segmented rather than blended into one metric: record tasks, D7 usage, payment and referral quality by group, then decide which use cases deserve focus.

Sources: [S15 Doubao official feature introduction](https://www.doubao.com/legal/feature_intro); [S16 Apple Intelligence developer introduction](https://developer.apple.com/cn/apple-intelligence/)


## Page 03 | Product & user journey

The product should connect understanding a request, processing information, producing an output, obtaining confirmation and following through.

| Capability | Intended experience | Engineering questions |
| --- | --- | --- |
| Conversation and voice | Describe a question or task directly | Model quality, voice cost and latency |
| Documents and search | Read files, extract information and retain sources | File limits, retrieval provenance and failures |
| Useful outputs | Lists, drafts, plans and summaries | Quality, editing and export |
| Tasks and memory | Retain approved preferences and task status | Permissions, accuracy, deletion and synchronization |
| Optional identity | Configurable character, voice, name and tone | Asset rights and consistent behavior |

### Example
“Read this event brief, list what I need to prepare this week, draft an announcement, and remind me on Friday to confirm.” The assistant explains its understanding, organizes the material, and produces a checklist and draft. The user confirms saving and reminders. External messages, payments and other consequential actions require confirmation of the specific action and permissions.

### Experience standard
Display an action as completed only after it succeeds. Tool failures should show a reason and next step. A personalized identity can make the product approachable, but cannot replace task quality. Reminders and alarms are part of the capability set, not the whole product.


## Page 04 | MVP & delivery scope

Keep the mass-market ambition, begin with extensible task capabilities, and agree the product and engineering boundaries with the team.

### Suggested first capability set — for joint selection
Text and limited voice interaction; document summaries with sources; drafts and plans; user-confirmed personal records; and one verifiable type of task execution. Character and tone remain configurable. The first release does not promise every system permission or complex automation to everyone.

| Candidate route | What it can test first | Team assessment needed |
| --- | --- | --- |
| Web / lightweight product | Sharing, task completion, price and channels | Background tasks, notifications, payment and mobile limits |
| Native / cross-platform app | Device capabilities and repeated everyday use | Store rules, permissions, build and maintenance effort |
| Staged combination | Core value first, then deeper device integration | Migration, account/data continuity and duplicate work |

### Validate capabilities before choosing technology labels
At least one set of real tasks must go from input to usable output. Include failure states, cost logs, data deletion and permission explanations. Test notifications and external actions separately. If the CNY 1 tier cannot support its cost, adjust allowances or the business model rather than quietly reducing the product to an alarm.

### Joint decision
I can prototype with AI. I want the team to assess reliability, performance, deployment and scaling with me; a personal prototype is not proof of readiness to serve 100,000 people.

Sources: [S13 Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/); [S16 Apple Intelligence developer introduction](https://developer.apple.com/cn/apple-intelligence/)


## Page 05 | Market sizing & evidence

Set targets at 1,000 / 10,000 / 100,000, while reporting activation, payment and continued use separately.

### Target definition
The stages refer to **genuinely activated users**: independently deduplicated people who complete at least one core task with a usable result. Track registrations, downloads, activation, payment and monthly activity separately. Downloads are not payers.

| Activation target | Payers at an assumed 20% conversion | What the stage must demonstrate |
| --- | --- | --- |
| 1,000 | 200 | Useful tasks, real payments and a functioning referral process |
| 10,000 | 2,000 | Repeatable acquisition, manageable retention/cost, limited manual intervention |
| 100,000 | 20,000 | Multiple channels, capacity, unit economics and stable operations |

### Market context versus growth targets
CNNIC's official indexed 2026 summary reports more than 700 million AI users in the first half of 2026. This indicates broad adoption, not an obtainable market share. The relevant paying segment is not yet measured. These stages are operating targets, not external forecasts.

### If the team wants targets to mean paying users
We can instead target 1,000 / 10,000 / 100,000 payers, but activation, funding and capacity must be recalculated together. At 20% conversion, 1,000 payers require 5,000 activated users. The two definitions cannot be mixed.

Sources: [S1 CNNIC: 2026 generative AI application report](https://www2.cnnic.cn/n4/2026/1008/c326-11703.html)


## Page 06 | Competition & alternatives

Strong general-purpose alternatives already exist. Low prices and referrals must be supported by sustained usefulness.

| Alternative | Existing capability / reference | Question for this product |
| --- | --- | --- |
| Doubao and other general AI assistants | Official introduction includes assistant, voice and text capabilities | Why switch? Is this simpler or better for daily tasks? |
| Apple Intelligence | Developer material covers personal context and app actions | What additional value exists across devices, audiences or experience? |
| A user's existing tool set | Search, documents, calendar, notes and AI chat | Does the product reduce steps and complete more tasks? |
| Character.AI / Replika | Established character or companion experiences | How does personalization strengthen usefulness beyond appearance? |

### First comparison
Use 10–20 frequent tasks. Ask users to try both their current tools and the prototype. Measure completion, elapsed time, edits, instructions required, cost and a second self-initiated use.

### Advantages to prove
Do not claim stronger models than major platforms, universally lower costs or an existing data moat without evidence. Test simpler access, executable tasks, continuous personal settings and accessible pricing. Referral incentives are an acquisition mechanism, not a durable product advantage by themselves.

Sources: [S3 Character.AI subscription page](https://character.ai/subscribe); [S5 Replika official product page](https://replika.com/); [S15 Doubao official feature introduction](https://www.doubao.com/legal/feature_intro); [S16 Apple Intelligence developer introduction](https://developer.apple.com/cn/apple-intelligence/)


## Page 07 | Business model & pricing

CNY 1 and CNY 10 remain pricing hypotheses. Discuss the first-payment reward separately from recurring subscriptions.

| Model | User payment | Direct-referral reward | Condition to test |
| --- | --- | --- | --- |
| A — accessible entry | CNY 1/month | CNY 1 once per genuine new payer's eligible first payment | Very low usage cost and sufficient renewal contribution |
| B — low-cost standard | CNY 10/month | CNY 1 once on the first payment | Enough product value for purchase and retention |
| C — first-month trial | CNY 1 first month, then 10/month | CNY 1 once on the first payment | Renewal at the full price after the initial experience |

### Interpretation of the proposed mechanism
A invites B. B first pays CNY 1 for the actual service; A receives a one-time CNY 1 reward. A may also invite C and D, earning separate rewards for their eligible first payments. People invited by B do not generate another tier of commission for A. The base model excludes a recurring CNY 1 reward; that is discussed separately below.

### Service and operating rules
Pricing must specify model, voice, file and task allowances, selected using measured costs and team input. Unlimited usage is not assumed. Rewards are proposed to settle after transaction validation and the refund observation period; instant receipt or unrestricted withdrawals are not promised.

### If CNY 1 is returned every month
For a CNY 1/month referred customer, the entire subscription's gross revenue would continue to be paid out while the platform still incurs costs. That subscription cannot fund its own service. A separate, identified revenue/subsidy source or a different reward amount/frequency would be required.

Sources: [S13 Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/); [S14 Ministry of Justice: Regulations on Prohibition of Pyramid Selling](https://xzfg.moj.gov.cn/front/law/detail?LawID=148)


## Page 08 | Unit economics & viability

Returning the full first CNY 1 leaves the platform funding the real cost of serving the acquired customer.

| Per new referred payer, CNY | A: 1/month | B: 10/month | C: first month 1 |
| --- | --- | --- | --- |
| First-month gross revenue | 1.00 | 10.00 | 1.00 |
| One-time direct reward | 1.00 | 1.00 | 1.00 |
| Processing 1% + refund reserve 3% | 0.04 | 0.40 | 0.04 |
| Assumed paid-user monthly service cost | 0.40 | 2.00 | 2.00 |
| First-month direct contribution | −0.44 | 6.60 | −2.04 |

CNY 0.40 and 2 are target costs to measure, not supplier quotations. The CNY 1 tier needs allowances compatible with its cost. A provisional split of 0.40 is model/tools 0.25, infrastructure 0.10 and support 0.05; the CNY 2 split is 1.50, 0.30 and 0.20. Each non-paying activated user additionally incurs an assumed CNY 0.10 for one capped trial month, not unlimited free service.

### Retention and channel sensitivity
A later paid month without a referral reward contributes 0.56 for A or 7.60 for B/C, before fixed costs, free trials and acquisition. If B's service cost rises to CNY 8, first-payment referred contribution falls to 0.60. With an applicable 30% channel deduction plus a 3% reserve, it is 3.70 for B and −2.33 for C.

### A low entry price does not eliminate expenditure
If all 1,000 new customers pay CNY 1 and all are referred, rewards total CNY 1,000, plus CNY 40 processing/reserve and service costs. Cap the experiment's funding before expanding it.


## Page 09 | The first 1,000 & growth stages

The first 1,000 need credible seed channels. Use measured referral performance to plan the next tenfold stage.

### From seed users to the first stage — planning assumptions
Use 100–200 seed users to test product quality and reward rules, then aim for 1,000 genuinely activated users. This answers the request for a concrete initial cohort without limiting the long-term ambition.

| Proposed seed channel | First-stage activations | Required action |
| --- | --- | --- |
| Five creator / community collaborations | 100 each; 500 total | Verify 20 prospects, demonstrate real task results and obtain trial agreement |
| Product demonstrations and content | 200 | Provide a usable experience and source attribution |
| Consented direct invitations and user sharing | 300 | Record task activation and eligible payments; deduplicate and detect abuse |

These channels are to be built. Existing followers or partner commitments have not been verified. Recalculate using actual sources rather than presenting candidates as signed partners.

### Users and payments
At 20% activation-to-payment conversion, 1,000 activations produce 200 payers. Assuming 70% are eligible referred payers, rewards total CNY 140. This means 140 qualifying first payments, not only 140 people seeing a shared link.

### Funnel and acquisition effort
Twenty partner prospects → ten substantive discussions → five agreed trials, using assumed 50% and 50% conversions. Five partner entries × 500 unique visits × 20% activation = 500 users; content generates 1,000 visits × 20% = 200; direct invitations and sharing generate 1,500 × 20% = 300. Total: 5,000 deduplicated visits → 1,000 activations → 200 payers. Attribute each person to their first valid source. None of these traffic volumes is committed.

The seed cash budget is CNY 1,000, implying a CNY 0.20-per-visit budget constraint that must be tested, plus CNY 140 rewards. Cash CAC = (1,000 + 140) ÷ 200 = CNY 5.70 per new payer. If outreach, demonstrations and attribution take 20 hours × CNY 80 = 1,600, acquisition CAC including that labor is CNY 13.70. This labor is allocated within the CNY 3,000 monthly fixed operating budget; do not deduct it twice.

Eligible referrals may originate in any of these channels. The 70% referred-payer assumption is a separate attribution dimension, not a claim that only the last channel supplies referred users.

### Stage gates
Before 1,000 → 10,000 → 100,000, reassess usage without incentives, retention, referred payments, consumption, capacity and funding. Set ambitious targets; let observed growth determine timing.


## Page 10 | CNY 1 referrals & the growth model

A CNY 1 incentive may encourage sharing. Growth depends on the number of genuine new payers produced by each generation.

### Referral formula
**K = share of payers who share × unique invitees per sharer × invitation-to-activation rate × activation-to-payment rate.** The denominator is the current generation of payers; the output is next-generation new payers. Count each invitee once.

| Scenario | Sharing | Unique invitees per sharer | Activation | Payment after activation | Paid referral coefficient K |
| --- | --- | --- | --- | --- | --- |
| Conservative | 30% | 3 | 40% | 20% | 0.072 |
| Neutral | 50% | 5 | 50% | 30% | 0.375 |
| Illustrative replacement condition | 100% | 5 | 50% | 40% | 1.000 |
| Growth experiment | 70% | 8 | 60% | 40% | 1.344 |

### Interpretation
K < 1 means successive referral generations decline without new seed acquisition. K = 1 approximately replaces the generation. K > 1 permits referral-led expansion under the assumptions. The highest value, 1.344, is an untested scenario, not measured performance.

### Timing also matters
A seven-day generation and a 30-day generation produce very different speeds at the same K. Overlapping networks, channel saturation, fake invitations, refunds and churn can reduce it. Do not promise “100,000 in a few days.” Report actual K, generation time, real retention and source mix at every stage.

### Attribution and settlement
Bind a direct link/code → complete a core task → genuine payment → refund observation and fraud review → record the reward → settle under agreed rules. The activity budget, per-person caps and withdrawal mechanism need team approval. This BP website does not take payments or operate a cashback program.


## Page 11 | Pricing & scale scenarios

Compare three prices across three cohort sizes to see whether growth also improves the economics.

All amounts in CNY.

| Activated cohort | Price model | Month-one revenue | First-payment rewards | Month-one economic result | 90-day cohort economic result |
| --- | --- | --- | --- | --- | --- |
| 1,000 | CNY 1/month | 200.00 | 140.00 | -4,108.00 | -9,974.72 |
| 1,000 | CNY 10/month | 2,000.00 | 140.00 | -2,700.00 | -6,891.20 |
| 1,000 | First month 1, then 10 | 200.00 | 140.00 | -4,428.00 | -8,619.20 |
| 10,000 | CNY 1/month | 2,000.00 | 1,400.00 | -14,080.00 | -28,747.20 |
| 10,000 | CNY 10/month | 20,000.00 | 1,400.00 | 0.00 | 2,088.00 |
| 10,000 | First month 1, then 10 | 2,000.00 | 1,400.00 | -17,280.00 | -15,192.00 |
| 100,000 | CNY 1/month | 20,000.00 | 14,000.00 | -70,800.00 | -117,472.00 |
| 100,000 | CNY 10/month | 200,000.00 | 14,000.00 | 70,000.00 | 190,880.00 |
| 100,000 | First month 1, then 10 | 20,000.00 | 14,000.00 | -102,800.00 | 18,080.00 |


### Shared assumptions — not a forecast
20% of activated users pay; 70% of new payers generate a one-time CNY 1 referral reward; monthly paid retention is 70%; free activated users incur only one capped CNY 0.10 trial month. Paid-user service costs are 0.40/month for A and 2/month for B/C. Processing is assumed at 1%, with a 3% refund reserve.

Monthly fixed operating economic costs are CNY 3,000 / 8,000 / 30,000 by stage; seed acquisition cash is 1,000 / 5,000 / 30,000. The 90-day calculation follows one cohort, with N, 0.7N and 0.49N payers across the months. It adds no later cohorts. The three stages must not be summed into a quarterly forecast.

### Result boundaries
Economic results deduct service, rewards, processing/refund reserve, fixed operations and seed acquisition. **They exclude common product development, unknown taxes, release/compliance costs and additional app-store commissions.** Positive results are not project net profit. A CNY 1 model may require continuing subsidy; a CNY 10 model depends on actual payment and retention, not the spreadsheet alone.

### If all targets mean payers
For 1,000 payers at CNY 1, first-month revenue is 1,000. If all are referred, rewards are also 1,000. Deduct 40 for processing/reserve and 400 for service: direct contribution is −440 before fixed costs and acquisition. Define the user target precisely.


## Page 12 | Resources & cash planning

Joint planning must cover funding and staffing at each scale as well as the technical route.

| Hypothetical new cohort | Monthly fixed operating economic cost | Seed acquisition cash | Model C first-month shortfall* |
| --- | --- | --- | --- |
| 1,000 activated / 200 payers | CNY 3,000 | CNY 1,000 | CNY 4,428 |
| 10,000 activated / 2,000 payers | CNY 8,000 | CNY 5,000 | CNY 17,280 |
| 100,000 activated / 20,000 payers | CNY 30,000 | CNY 30,000 | CNY 102,800 |

*Model C charges CNY 1 in month one, then 10/month. Shortfall is operating revenue less service, rewards, fees, fixed operations and acquisition, before development. Fixed cost includes labor valued economically; payment timing must still be separated. These figures do not establish the minimum bank balance required.

### Estimate construction before requesting quotations
An existing prototype can support early tests. An illustrative 200–400 engineering hours × CNY 150 gives 30,000–60,000; 100–200 product hours × 80 adds 8,000–16,000. The total 38,000–76,000 is a range example, not an approved budget. Re-estimate after platform, payment, task integrations, review and store-release scope are chosen.

### Scaling decisions
Confirm the pricing model and measured task costs, then test peak concurrency and success rates. Approve the budget for each stage before expanding. Rewards create settlement obligations and timing gaps; identify funding and redemption limits before the campaign.


## Page 13 | 90-day milestones

Connect product and growth stages through evidence-based gates agreed with the team.

| Stage | Product and market work | Evidence for progression |
| --- | --- | --- |
| Weeks 1–2 | Agree core tasks, route and allowances; test product and reward rules with 100–200 seed users | Usefulness, costs and event tracking can be measured |
| First 1,000 activated users | Controlled, attributable recruitment; test CNY 1 / 10 pricing and actual payments | Task completion, D7, payment and valid referrals |
| Move toward 10,000 | Expand validated channels; observe mature renewals and generation K; load-test | Unit economics, retention and quality remain acceptable |
| Move toward 100,000 | Multiple channels, monitoring, support and funding; scale in batches | Sustainable operation, fundable rewards and no major quality gaps |
| Day-90 review | Report only achieved stages and mature observation periods | Set the next target, budget and scope |

### Dates are not promises made in advance
The team can discuss a 90-day scale target, but 100,000 is not a guaranteed forecast without seed, K and generation-time evidence. Users not yet due to renew are not churned; late cohorts do not receive a fictional full 90-day observation.

### My position
I want to set a larger ambition and personally advance the experience, content, channels and feedback. I want to work out reliable execution with the team rather than privately guessing the entire implementation route.


## Page 14 | Metrics & acceptance criteria

Measure real tasks, sustained use and payment alongside growth, rather than counting reward-seeking accounts alone.

| Metric | Denominator / window | Initial threshold for discussion* |
| --- | --- | --- |
| Core-task success | Independent users who actually start a task | At least 80% get a usable result; record failures |
| D7 task activity | Activated users whose day 7 has arrived | At least 30%; reward-page visits do not qualify |
| First-payment conversion | Actual first payers / activated users | Test the 20% assumption separately by price |
| Monthly paid renewal | Payers whose renewal date has arrived | Model assumes 70%; diagnose actual rates below 60% |
| Referral K and generation time | Next-generation new payers produced by current payers | Measure weekly; K > 1 does not imply unlimited growth |
| Variable cost | Models, tools, voice, support, processing and rewards | Within approved usage and subsidy limits |

*These are management hypotheses for team discussion. Separate price and free-allowance cohorts; do not use CNY 1 conversion as evidence for CNY 10.

### Continue / adjust / pause
If task value and retention work but economics do not, adjust price, allowances or rewards. If incentives generate registrations without use, revise the product and audience. Pause expansion when budget, refunds or invalid transactions exceed agreed limits. Resolve consequential permission or execution failures before using growth as justification to continue.


## Page 15 | Risks & responses

Use transparent rules to manage promotion and service costs; a small transaction can create a large cumulative obligation.

| Risk | Condition to check | Response |
| --- | --- | --- |
| Rewards consume revenue | Service costs remain after returning the first CNY 1 | Budget subsidy, test renewal contribution or change rewards |
| Fake payments / self-referrals | Account, device, payment and refund anomalies | Reward only genuine eligible new customers; observation period and appeal |
| Platform and launch rules | Specific platform, region, payment route and reward mechanics | Check applicable rules and professional advice before finalizing launch |
| Payment buys recruitment eligibility | Purchasing is framed as joining a referral-income network | Ensure genuine service value; no paid recruiting qualification or tiered commissions |
| Cost and capacity | Heavy usage, tool failures and traffic spikes | Allowances, monitoring, load tests and transparent failures |
| Personal data and execution | Memory, documents and external-action permissions | Least privilege, explicit confirmation, deletion and access logs |

### Scope of rules review
Apple has rules concerning paid functionality and incentives. Application depends on region and mechanics; do not assume paid installation plus cash referrals can launch unchanged. China's Regulations on Prohibition of Pyramid Selling address, among other situations, payment for recruiting eligibility and compensation based on recruitment or levels. A single level does not automatically establish compliance; the actual structure requires professional assessment.

This review informs a workable version of the growth concept. It does not replace the business discussion. No cashback program is open and no money has been collected through this BP.

Sources: [S13 Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/); [S14 Ministry of Justice: Regulations on Prohibition of Pyramid Selling](https://xzfg.moj.gov.cn/front/law/detail?LawID=148)


## Page 16 | Team roles & collaboration

I will lead product and market execution, while assessing technical choices and resources jointly with the team.

### My proposed responsibilities
I will own everyday needs and task experience, pricing and referral experiments, channel content and user feedback. I can rapidly prototype and prepare experiments with AI, and want to assess reliability, costs and scalable implementation with engineering. A prototype is not proof of production-service readiness.

| Role | Proposed responsibility | To confirm |
| --- | --- | --- |
| 最高 | Product, customers/users, market work, experiments and review | Availability and stage targets |
| Engineering lead | Architecture, models/tools, permissions, tasks and cost logs | People, hours, schedule and maintenance |
| Professional / content reviewer | Facts, asset rights and output quality | Reviewer, competence, price and scope |
| Customer / user | Usable material, confirmation, feedback and acceptance | Consent and intended use |
| Team247 lead | Budget, resources, payment/contract entity and stage decisions | Authority and available resources |

### Decisions to make together
Launch platform, core tasks, models/tools, usage budget, data handling, release requirements, price, responsibilities and acceptance. Joint discussion is not an excuse to provide no proposal: this BP offers comparable assumptions and experiments for the team to revise.

### Working cadence
Review real activations/customers, payments/refunds, output quality, effort/API costs and next-week decisions weekly. Record a continue/adjust/pause decision at days 14 and 30. These are proposals, not staffing or budget commitments already obtained.


## Page 17 | Evidence, assumptions & unknowns

Public sources support context and constraints. Project revenue and growth remain unverified assumptions.

| Evidence | Date and limits |
| --- | --- |
| [S1 · CNNIC: 2026 generative AI application report](https://www2.cnnic.cn/n4/2026/1008/c326-11703.html) | Published 2026-10-08; first half of 2026. Official indexed summary only; direct body retrieval timed out. More than 700 million AI users is context, not the size of this paying segment. |
| [S13 · Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/) | Checked 2026-11-09. Paid functionality, incentives and store rules need assessment for the relevant region and actual mechanism; cash rewards cannot be assumed launchable unchanged. |
| [S14 · Ministry of Justice: Regulations on Prohibition of Pyramid Selling](https://xzfg.moj.gov.cn/front/law/detail?LawID=148) | Searched 2026-11-09. Recruiting eligibility purchased through payment and compensation linked to recruitment or levels require assessment. A single referral level does not automatically establish compliance. |
| [S15 · Doubao official feature introduction](https://www.doubao.com/legal/feature_intro) | Official indexed summary checked 2026-11-09. Assistant, voice and text capabilities. No pricing or user data from imitation websites is used. |
| [S16 · Apple Intelligence developer introduction](https://developer.apple.com/cn/apple-intelligence/) | Official indexed summary checked 2026-11-09. Personal context, app actions and system entry points are competitive references. Region/device availability requires separate verification. |

### Critical gaps
Verified audience/channel figures; real CNY 1/10 conversion; referral K and generation time; monthly retention; measured task cost; executable reward rules; technical and staffing quotations.

### Replace assumptions with evidence
Use sourced prospect records, interviews, payment/refund records, task logs, supplier invoices and mature-cohort observations. Mark missing evidence as unverified; do not invent customers, case-study revenue, permissions or testimonials.

### Evidence levels
Public facts retain their sources and dates. Prices, counts and costs are planning assumptions. Formula outputs are calculations. Relationships, resources and technical capability remain to be validated. Recheck dynamic prices before launch. The BP and website are deliverables; commercial viability has not been established.

Sources: [S1 CNNIC: 2026 generative AI application report](https://www2.cnnic.cn/n4/2026/1008/c326-11703.html); [S13 Apple App Review Guidelines](https://developer.apple.com/app-store/review/guidelines/); [S14 Ministry of Justice: Regulations on Prohibition of Pyramid Selling](https://xzfg.moj.gov.cn/front/law/detail?LawID=148); [S15 Doubao official feature introduction](https://www.doubao.com/legal/feature_intro); [S16 Apple Intelligence developer introduction](https://developer.apple.com/cn/apple-intelligence/)


## Page 18 | Recommendation & decisions

If the team wants a scalable consumer opportunity, prioritize discussion of personal AI and the first stage of investment.

### Proposed direction
I want to work with the team on a personal AI assistant ordinary people can use, with 1,000 → 10,000 → 100,000 genuine users as staged goals. CNY 1/10 prices and referrals are starting models for joint revision.

| Decision | Proposal supplied | Team judgment needed |
| --- | --- | --- |
| Product | Frequent tasks + personal continuity + optional identity | First core tasks and platform |
| Price | 1/month, 10/month, or first month 1 then 10 | Allowances, value and pricing tests |
| Acquisition | One CNY 1 reward per eligible direct new payer | Executable rules, budget and settlement |
| Scale | 1,000 / 10,000 / 100,000 activations | Timing, staffing, capacity and gates |
| Technical route | Lightweight web, app or staged combination | Engineering estimates, models and integrations |

### First action
Use 100–200 seed users to test tasks and mechanics, then pursue the first 1,000 activations. Expand only after checking real tasks, retention, cost and reward settlement. Without confirmed funding and engineering, do not claim readiness for 100,000 users.

### Different strategic objectives
For near-term payment and bounded delivery, the industry agent is more direct. For a mass-market product opportunity, this direction deserves priority discussion. Team feedback should identify the preferred objective, available resources and most uncertain assumptions so we can choose a route together.


# 02 AI agent for medical aesthetics


## Page 01 | Executive summary

Charge for one clearly defined industry task, then validate review quality, total time saved and renewal.

| Business item | Pilot proposal |
| --- | --- |
| Product | Turn medical-aesthetics product material into sourced, reviewable copy and template assets |
| Customer / payer | Institution or brand teams with recurring tasks, a reviewer and purchasing budget |
| Pricing hypothesis | CNY 2,980 for a 14-day pilot; CNY 1,980/month after qualification |
| Initial target | 200 prospects → 120 valid contacts → 36 meetings → 10 paid pilots |
| Base 90-day revenue | CNY 37,720; three subscribers at period end; MRR 5,940 |
| Economic result | CNY −24,188.80 including internal labor; no promise of quarterly payback |

### Original concept and initial scope
Retain document retrieval, content production, institution research and business workflows. Start with traceable content delivery. Custom work for other industries is priced independently; hypothetical large contracts do not subsidize the standard-product forecast.

### Decision requested
Choose one customer group, one source set, a professional reviewer and capped pilot resources. I will advance customers, product and market work; integrations and engineering investment will be assessed jointly with the team.


## Page 02 | Customers & the problem

The user, reviewer and budget owner are different roles. All three must be identified.

| Role | Assumed current problem | Product response | Purchasing question |
| --- | --- | --- | --- |
| Content / operations | Repeated research, revisions and version confusion | Generate sourced drafts and template graphics from controlled material | Does editing effort actually fall? |
| Professional reviewer | Unsupported statements and confused applicability | Inspect sources, conflicts and revision history | Can conclusions be traced and unsupported claims rejected? |
| Business owner | Unpredictable labor and supplier delivery | See time, outputs and acceptance records | Is measurable value greater than price? |
| Brand development | Inaccurate institution lists and slow research | Review 50 public target institutions and matching reasons | Are these qualified leads, without a sales guarantee? |

A qualified pilot customer has recurring content tasks; can supply usable material; appoints both a reviewer and business owner; provides a workflow baseline; and can authorize CNY 2,980. General curiosity about AI is insufficient.

### Exclusions
No actual task, no usable source material, no reviewer, no budget authority, or a request to replace clinical decisions means no paid pilot. Start by reconstructing a recent real task, not asking whether the prospect wants AI.


## Page 03 | Product & user journey

Value comes from a complete workflow for sources, versions, review and deliverables.

### From source material to a usable output
Confirm model / market version / intended use → import authorized material → record provenance and update dates → retrieve and draft with citations → professional review → template layout → customer acceptance → version archive.

### Example
A customer requests a 500-Chinese-character product brief. Confirm the exact product and version instead of inferring intended users from the brand. List source conflicts or missing evidence. The reviewer removes unsupported statements and preserves provenance before graphics are prepared. Measure generation, verification and editing together.

| Capability | What the customer receives | What cannot yet be claimed |
| --- | --- | --- |
| Retrieval | Sourced facts and explicit gaps | A comprehensive proprietary industry moat |
| Drafting | Reviewable copy or scripts | Automatically lawful publication |
| Institution research | Deduplicated organizations, public business entry points and matching reasons | An email address equals a qualified opportunity |
| Custom workflow | Tools and acceptance within a defined scope | Universal applicability or unlimited customization |

Public institution research is a separate add-on experiment. The customer reviews and contacts prospects through permitted channels; messages sent are not sales.

Sources: [S10 Medical-aesthetics advertising enforcement guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2023/art_d1b46dbc27214abcace53a0ec539f7bb.html); [S11 Medical advertising supervision guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2025/art_cd56662cf13b4ad59eabfe31cb1122e1.html)


## Page 04 | MVP & delivery scope

The CNY 2,980, 14-day pilot needs a finite scope and itemized acceptance.

The package covers one brand/business line, one source collection and one review process. Limit sources to 30 documents and 200 total pages; long scans, complex tables or additional products require assessment. Deliver: one versioned source index; ten sourced task outputs, each one piece of copy or a script; three template graphics; one Q&A and boundary-rule set; one training session; and a before/after time report. Allow up to two consolidated revision rounds within the agreed scope, not repeated changes of requirements.

Exclude automatic publishing, diagnosis, medical-record handling, unsupported efficacy promises, guarantees of advertising legality, autonomous sales, deep CRM integrations and custom films. Outputs are review drafts. The customer and qualified professionals must verify publication eligibility and applicable review procedures. Official medical-aesthetics and 2025 medical-advertising guidance support retaining evidence and review records; human checking is not regulatory approval. See S10 and S11.

For a specific 500-character product brief, confirm model, market version, material date and intended use. Missing evidence is a gap, not permission to invent indications. Retrieve and attach sources, review unsupported statements, prepare template graphics, obtain business acceptance and archive the version and reviewer. Do not deliver fabricated patient cases or images represented as real treatment outcomes.

Sources: [S10 Medical-aesthetics advertising enforcement guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2023/art_d1b46dbc27214abcace53a0ec539f7bb.html); [S11 Medical advertising supervision guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2025/art_cd56662cf13b4ad59eabfe31cb1122e1.html)


## Page 05 | Market sizing & evidence

Size the serviceable segment through customer qualification and verified prospects, not all hospitals multiplied by a subscription price.

**Public context:** China reported 38,710 hospitals, including 26,956 private hospitals, at year-end 2024. These are all-hospital counts, not medical-aesthetics providers. Clinics, outpatient facilities, institutional groups and brands also have different purchasing entities.

| Level | Definition for this project | Current evidence |
| --- | --- | --- |
| TAM | Target institutions/brands with content budget, source material and professional review | Segment total not verified |
| SAM | Remote/local serviceable teams, typically 3–10 operations staff with recurring tasks | Requires directory screening and interviews |
| Proposed prospect list | 40 introductions to confirm + 100 public listings + 60 channel candidates | 200 is a list-building target, not current customers |
| 90-day contact | 200 × 60% valid contact = 120 | Requires substantive two-way response |
| Delivery capacity | Base ten pilots; at most two active together | Constrained by 14 direct service hours per pilot |

### Financial scale
Ten pilots and four subscription customer-months generate CNY 37,720 in the base case. Pilot fees are not MRR; three period-end subscribers imply MRR of 5,940. Additional cash budget is 15,828.80; total economic expenditure is 61,908.80.

### Evidence collection
Verify 30 purchasing entities and their public sources in week one, then build toward 200. Deduplicate entities within the same purchasing group. Interest in AI is not qualified procurement demand.

Sources: [S2 National Health Commission: 2024 statistical bulletin](https://www.nhc.gov.cn/guihuaxxs/c100132/202512/9db8db5488a748c4b1e1068a4a8c4455.shtml?menuid=128)


## Page 06 | Competition & alternatives

General tools already support workflows. We must demonstrate more reliable industry delivery and lower total effort.

| Alternative | Public reference | Additional value to prove |
| --- | --- | --- |
| Dify | Annual Professional USD 590/workspace; Team USD 1,590; knowledge and workflow tools | Source preparation, review, task templates and service |
| Coze | Subscription/credit tiers; individual, team and enterprise; notice of new-plan changes on November 12 | Traceable, acceptable outputs rather than an agent interface alone |
| General model + human editor | A customer's current alternative | Better total time and fact checking, not just faster generation |
| Agencies / custom developers | Existing delivery approaches; actual quotes to obtain | Scope, cost and repeatability |

### Comparison design
Use five real tasks with identical sources and objectives. Compare a general model plus documents against the proposed workflow. Where possible, blind the reviewer to the method. Record factual errors, source coverage, revision rounds and total labor. The knowledge base is a proposed asset, not an established moat.

### Why a customer would buy
Customers may pay for dependable results and convenience without caring whether the software is called an agent. If an internal technical team can build more cheaply, acknowledge that the organization may not be a priority customer.

Sources: [S6 Dify official pricing](https://dify.ai/pricing); [S7 Coze official plans and pricing](https://docs.coze.cn/cozespace_coze_billing_overview)


## Page 07 | Business model & pricing

Price pilots, subscriptions, public institution research and custom implementation separately.

| Offer hypothesis | Price / cycle | Scope and payment |
| --- | --- | --- |
| Content-workflow pilot | CNY 2,980 / 14 days | 50% at start, 50% on agreed acceptance; remediate or address unfulfilled scope under contract |
| Standard subscription | CNY 1,980 / institution / month | Three seats, 30 text tasks, ten template graphics, 100 retrievals, up to one hour supplier professional review and four hours operations support; final review belongs to the customer |
| Public institution research add-on | CNY 980 / batch | 50 deduplicated institution records, public business entry points and sample-check report; no bulk outreach or response/sales guarantee; excluded from base revenue |
| Extra implementation | From CNY 3,000, after assessment | New source migration, templates or interfaces; quote effort and acceptance first |
| Other-industry customization | Pricing experiment from CNY 19,800 | One workflow and one system interface; narrow or reprice if estimated total cost exceeds 11,880 |

The subscription's 30 drafts allow limited revision; they do not include complete supplier medical review of every item. One review hour covers sampling or consolidated questions. Full per-item review needs extra budget. Stop at allowance limits and notify the customer rather than charging automatically.

CNY 19,800 is neither an established market price nor an accepted negotiation outcome. A 40% / 40% / 20% payment structure can be discussed for kickoff, working prototype and acceptance. Confirm interfaces, data permission, maintenance and scope changes first. Standard 90-day revenue excludes custom contracts; customization is not MRR.

### Work back from customer ROI
If a task falls from 90 to 45 minutes including review, 30 tasks save 22.5 hours/month. At CNY 80/hour, this is only 1,800, below the 1,980 fee. Time savings alone require at least 49.5 minutes saved per task, a higher actual hourly cost or more tasks. Other value must be measured, not filled in with assumed sales growth. Obtain each customer's baseline.


## Page 08 | Unit economics & viability

Direct contribution is CNY 1,480.80 per pilot. Doubling delivery time can make the result after acquisition negative.

| Cost, CNY | 2,980 pilot | 1,980 subscription customer-month |
| --- | --- | --- |
| Product / operations | 12 hours × 80 = 960 | 4 hours × 80 = 320 |
| Professional review | 2 hours × 150 = 300 | 1 hour × 150 = 150 |
| Models / customer storage | 120 | 130 |
| Direct service cost | 1,380 | 600 |
| Processing 1% + loss reserve 3% | 119.20 | 79.20 |
| Direct contribution | 1,480.80 | 1,300.80 |

### Customer-value check
Saving 45 minutes on each of 30 tasks at CNY 80/hour is worth 1,800, less than the monthly fee. At least 49.5 minutes per task, higher actual labor costs or more tasks are needed to justify purchase from time savings alone. Do not fill the gap with unproven incremental sales.

### Sensitivity
If pilot operations increase from 12 to 24 hours, contribution falls to 520.80. After full CAC of 880, the result is −359.20. At a reduced subscription price of 1,280 with unchanged service cost, monthly contribution is 628.80. Recurring common operations/maintenance of 7,000/month require six continuing subscribers, or eight when one-year construction amortization is included. The base case ends with only three.


## Page 09 | Acquiring the first customers

Ten paid pilots must come from a verifiable funnel. They are a validation batch, not a long-term ceiling.

Base funnel: **200 deduplicated prospects × 60% valid contact × 30% completed needs meeting × 30% pilot purchase ≈ 10.8**, rounded down and capacity-capped at ten. “Valid contact” means substantive two-way contact, not delivery of a message. Meeting conversion is measured over 120 contacted prospects; purchase conversion over 36 completed meetings.

| Proposed source | Target list size | Verification | First action |
| --- | --- | --- | --- |
| Confirmed usable industry relationships / AI-consulting introductions | 40 | Verify relationship, role and willingness to introduce; no assumed access to a private address book | Request a 20-minute workflow interview |
| Official directories, websites and public business entry points | 100 | Verify organization, region, content activity and contact route; deduplicate buyers | Prepare a short sample around one public task |
| Brands, training and industry-service partners | 60 | Confirm introduction capability and commercial arrangements | Show a reviewable before/after comparison |

This is not a completed customer list. Verify 30 real prospects in week one and 60 by week two; lower the quarterly target if suitable prospects cannot be found. Each row needs organization, region, business line, public source URL, user department, budget owner, confirmed introduction status, next action and do-not-contact flag.

### Draft opening message — not sent
“We are testing a workflow that turns product material into sourced content drafts. I would first like to understand the time you spend finding information, writing and reviewing. If there is a suitable task, we can demonstrate a limited comparison. Only after confirming value, source rights and acceptance would we discuss a paid 14-day pilot.”

Plan 60 sales hours over 90 days: 20 for research, about 18 for 36 meetings, and 22 for follow-up/proposals. Cash budget: CNY 4,000 for samples, travel/online events and small channel trials. More than six minutes of verification per prospect exhausts the research allocation for 200 prospects; narrow the geography or add effort. AI does not make acquisition free. Use permitted personalized contact routes and honor opt-outs; do not bulk-add private phone numbers on WeChat.

Deliver two pilots in month one, four in month two and four in month three, with at most two active concurrently. Ten pilots need 140 direct service hours, excluding sales and common development; each subscription customer-month adds five. Reduce concurrency if two pilots cannot be delivered within 14 days.


## Page 10 | Channels & sales process

Diagnose a real task before demonstrating, quoting, collecting payment and accepting delivery.

| Period | Action | Evidence / next step |
| --- | --- | --- |
| Week one | Verify 30 prospects; conduct five interviews | Recent task, user, payer and source rights |
| Week two | Reach 60 prospects, 15 interviews and five matched-task comparisons | Seek two pilot kickoff payments |
| First delivery | Agree scope; collect 50% upfront; deliver in 14 days; remaining 50% on acceptance | Retain outputs and actual receipts, not invoices alone |
| Renewal | Present the comparison report and bounded 1,980/month specification | Actual renewal from due customers |
| Channel expansion | Turn accepted, consented work into a case; replicate outreach | Record introductions and new outcomes separately |

### Draft contact wording
“I would like to understand how long research, writing and review currently take. We can compare one de-identified task, confirm value and acceptance, and then discuss a paid 14-day pilot.” This is a proposed draft, not a message sent in this task.

### Channel boundaries
A list is not a customer base; a public contact is not consent for bulk messaging. Record opt-outs. Do not collect private phone numbers for mass WeChat additions. The base plan provides CNY 4,000 and 60 sales hours; narrow the region or revise the budget if verification takes longer.


## Page 11 | Financial scenarios

Apply the same formula to conservative, base and upside cases. More revenue does not mean total investment has been recovered.

All amounts in CNY.

| Scenario | 90-day revenue | Direct contribution | Cash expenditure budget | Full economic result |
| --- | --- | --- | --- | --- |
| Conservative | 10,920.00 | 5,743.20 | 9,976.80 | -37,456.80 |
| Base | 37,720.00 | 20,011.20 | 15,828.80 | -24,188.80 |
| Upside | 60,540.00 | 32,618.40 | 21,961.60 | -13,581.60 |


| Input | Conservative | Base | Upside |
| --- | --- | --- | --- |
| Prospects / valid-contact rate | 120 / 50% | 200 / 60% | 300 / 70% |
| Meeting / pilot-purchase rate | 25% / 20% | 30% / 30% | 35% / 35% |
| Delivered-pilot capacity | 3 | 10 | 15 |
| Total subscription customer-months | 1 | 4 | 8 |

Base revenue = 10 × 2,980 + 4 × 1,980 = CNY 37,720. The upside funnel can produce more demand, but delivery is capped at 15 pilots. All scenarios remain below full construction and selling costs. Additional cash assumes internal hours are not paid incrementally. Unquoted taxes and similar items are excluded.


## Page 12 | Resources & cash planning

Internal engineering and product resources have an economic cost even when no immediate cash payment occurs.

| Common investment | Planning cost, CNY |
| --- | --- |
| Engineering: 160 hours × 150 | 24,000 |
| Product: 80 hours × 80 | 6,400 |
| One-time test setup | 2,000 |
| Common infrastructure and administration, three months | 3,000 |
| Total fixed economic investment | 35,400 |

### Additional workload
The base case needs 140 direct service hours for ten pilots, 20 for four subscription customer-months, and 60 for sales. Assign these by role and individual availability; do not assume a part-time engineer can perform everything.

### Cash timing
Additional cash budget is 15,828.80; total economic expenditure is 61,908.80. Proposed pilot payments are 50% upfront and 50% on acceptance. Sales, API and review expenses may precede receipts, so plan working capital by actual payment dates. Contract value is not money received. If all planned revenue is collected, the cash balance difference is positive while the full economic result remains negative.

### First 14 days
If the team chooses industry work for near-term paid validation, discuss an additional cash cap of 5,000, 35 hours from me, 20 engineering hours and ten professional-review hours. Review cash is included in the cap; do not add it again. This allocation has not been approved.


## Page 13 | 90-day milestones

Expand delivery in batches. Let actual acceptance and renewal from mature customers determine productization.

| Checkpoint | Proposed task / target | Evidence for continuing |
| --- | --- | --- |
| D7 | Verify 30 prospects, five interviews and a reviewer | Actual tasks and usable material |
| D14 | 15 interviews, five comparisons, seek two kickoff payments | Paid acceptance of bounded scope |
| D30 | Complete the first two pilots | Acceptance, controlled effort and errors |
| D60 | Deliver four more; target actual renewal from at least two mature customers | Payments from due cohorts, not verbal intent |
| D90 | Deliver four more; base case ends with three subscribers | Recalculate service, CAC and subscription contribution |

### Quarterly base definition
New pilots are delivered 2 / 4 / 4 by month. Period-end subscriptions are 0 / 1 / 3, totaling four customer-months. Month-three pilots not yet due for renewal are neither churned nor successful renewals.

### Capacity constraint
At most two active pilots, each lasting 14 days. If the first two cannot meet scope, reduce concurrency or raise price before expanding outreach. D0 begins when the team confirms resources.


## Page 14 | Metrics & acceptance criteria

Measure expertise, time saved, payment and renewal separately. Replication requires all of them.

Run five real matched-task comparisons with the same customer material and task: general model plus sources versus the workflow system. Blind the reviewer to the method where practical. Record total time, verification time, factual errors, source coverage, edits and usable-output rate. Generation speed alone is insufficient.

Suggested pilot acceptance: all ten agreed outputs delivered; every verifiable product fact has a supporting source or an explicit gap; no unresolved critical factual errors; sampled links open and substantiate their sentences; median total task time falls by at least 30%; all review/revision versions are traceable; and at least 80% of outputs meet pre-agreed usability standards within two rounds. No sales or regulatory-publication approval is guaranteed.

Continuation gates: at least two agreed kickoff payments by D14; two accepted pilots by D30; at least two real renewals among mature customers by D60. Ten paid pilots by D90 is a target; three period-end subscribers is the base assumption. Pause productization if 20 qualified interviews yield fewer than two willing payers, the first three pilots consistently exceed 24 direct hours, or usable source rights / professional review cannot be secured. Narrow the service or stop.

Validate the institution-research module separately: 50 deduplicated records with traceable sources; sample at least ten; target at least 90% correctness for institutions and contact entry points. An email is not a qualified opportunity. Observe the customer's permitted outreach, responses, meetings and conversion. This project does not send bulk messages. Keep the module out of the main subscription pitch until value is demonstrated.


## Page 15 | Risks & responses

Industry errors and uncontrolled human service effort matter more than the ability to generate text.

| Risk | Early signal | Response / owner |
| --- | --- | --- |
| Incorrect or stale sources | Confused model/version; citation fails to support a claim | Engineering preserves versions; reviewer checks; stop generation when evidence is inadequate |
| Advertising / clinical boundaries | Efficacy guarantees or unverified applicability | Customer and reviewer confirm intended use; no automatic publishing |
| Uncontrolled labor | First three pilots repeatedly exceed 24 hours | I narrow scope, reprice or pause productization |
| Weak renewal | Value below 1,980 or no recurring task | Reassess actual ROI; no unlimited support sustained by discounts |
| Low sales efficiency | Fewer than two willing payers after 20 qualified interviews | Narrow the audience or stop before building a platform |
| Failed data separation | Cross-customer retrieval or unclear permission | Engineering suspends affected access and investigates scope |

### Professional checking is not administrative approval
The operating business must verify publication eligibility and applicable review requirements. Software supports provenance, review and records. My industry experience does not replace all professional verification of product facts.

### Accountability
I own customer scope; engineering owns permission and logs; the reviewer checks facts; the customer owns final use and publication decisions. Agree fees, permissions and integration boundaries before contracting.

Sources: [S10 Medical-aesthetics advertising enforcement guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2023/art_d1b46dbc27214abcace53a0ec539f7bb.html); [S11 Medical advertising supervision guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2025/art_cd56662cf13b4ad59eabfe31cb1122e1.html)


## Page 16 | Team roles & collaboration

I will lead product and market execution, while assessing technical choices and resources jointly with the team.

### My proposed responsibilities
I will own industry customers, source/content standards, quotation scope, sales and delivery reviews. I can rapidly prototype and prepare experiments with AI, and want to assess reliability, costs and scalable implementation with engineering. A prototype is not proof of production-service readiness.

| Role | Proposed responsibility | To confirm |
| --- | --- | --- |
| 最高 | Product, customers/users, market work, experiments and review | Availability and stage targets |
| Engineering lead | Architecture, models/tools, permissions, tasks and cost logs | People, hours, schedule and maintenance |
| Professional / content reviewer | Facts, asset rights and output quality | Reviewer, competence, price and scope |
| Customer / user | Usable material, confirmation, feedback and acceptance | Consent and intended use |
| Team247 lead | Budget, resources, payment/contract entity and stage decisions | Authority and available resources |

### Decisions to make together
Launch platform, core tasks, models/tools, usage budget, data handling, release requirements, price, responsibilities and acceptance. Joint discussion is not an excuse to provide no proposal: this BP offers comparable assumptions and experiments for the team to revise.

### Working cadence
Review real activations/customers, payments/refunds, output quality, effort/API costs and next-week decisions weekly. Record a continue/adjust/pause decision at days 14 and 30. These are proposals, not staffing or budget commitments already obtained.


## Page 17 | Evidence, assumptions & unknowns

Public sources support context and constraints. Project revenue and growth remain unverified assumptions.

| Evidence | Date and limits |
| --- | --- |
| [S2 · National Health Commission: 2024 statistical bulletin](https://www.nhc.gov.cn/guihuaxxs/c100132/202512/9db8db5488a748c4b1e1068a4a8c4455.shtml?menuid=128) | Published December 2025; year-end 2024 statistics. 38,710 total hospitals and 26,956 private hospitals. These are not medical-aesthetics institution counts. |
| [S6 · Dify official pricing](https://dify.ai/pricing) | Dynamic page; checked 2026-11-09. Annual Professional USD 590/workspace and Team USD 1,590. These are not the total cost of an industry service. |
| [S7 · Coze official plans and pricing](https://docs.coze.cn/cozespace_coze_billing_overview) | Checked 2026-11-09; page announces changes on November 12. Subscriptions and credits. Near-term price changes mean these are not a fixed long-term API cost. |
| [S10 · Medical-aesthetics advertising enforcement guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2023/art_d1b46dbc27214abcace53a0ec539f7bb.html) | 2021 guidance; migrated official page. Qualifications, review and content restrictions. Human checking is not regulatory approval. |
| [S11 · Medical advertising supervision guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2025/art_cd56662cf13b4ad59eabfe31cb1122e1.html) | Published May 2025. Informs advertising-review boundaries; it is not a compliance determination for this product. |

### Critical gaps
A real 200-prospect list; professional review capacity; current customer effort and budgets; actual payments/renewals; API/deployment quotations; repeatable delivery effort.

### Replace assumptions with evidence
Use sourced prospect records, interviews, payment/refund records, task logs, supplier invoices and mature-cohort observations. Mark missing evidence as unverified; do not invent customers, case-study revenue, permissions or testimonials.

### Evidence levels
Public facts retain their sources and dates. Prices, counts and costs are planning assumptions. Formula outputs are calculations. Relationships, resources and technical capability remain to be validated. Recheck dynamic prices before launch. The BP and website are deliverables; commercial viability has not been established.

Sources: [S2 National Health Commission: 2024 statistical bulletin](https://www.nhc.gov.cn/guihuaxxs/c100132/202512/9db8db5488a748c4b1e1068a4a8c4455.shtml?menuid=128); [S6 Dify official pricing](https://dify.ai/pricing); [S7 Coze official plans and pricing](https://docs.coze.cn/cozespace_coze_billing_overview); [S10 Medical-aesthetics advertising enforcement guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2023/art_d1b46dbc27214abcace53a0ec539f7bb.html); [S11 Medical advertising supervision guidance](https://www.samr.gov.cn/zw/zfxxgk/fdzdgknr/ggjgs/art/2025/art_cd56662cf13b4ad59eabfe31cb1122e1.html)


## Page 18 | Recommendation & decisions

If the immediate objective is to validate payment and delivery, the industry agent is the more direct first pilot.

### Why it fits near-term validation
A budget owner is easier to identify, task frequency and time savings are measurable, and delivery can begin with human assistance. It can validate real revenue without establishing national segment size, standardized subscriptions or long-term growth.

| Decision | Suggested starting point |
| --- | --- |
| Customer and task | One reachable region/segment and one product-content workflow |
| 14-day objective | 15 substantive interviews, five comparisons, seek two kickoff payments |
| Cash and effort | Discuss a CNY 5,000 additional cash cap and named staffing; not an approved budget |
| Price | Bounded 2,980 pilot, then test 1,980/month |
| Continue when | Real acceptance, time savings, manageable cost and mature-customer renewal |
| Pause when | Fewer than two willing payers after 20 qualified interviews, no reviewer or uncontrolled effort |

### Relationship to personal AI
The industry pilot can test team collaboration and paid delivery. Personal AI addresses a different consumer-growth opportunity. Windows, customer counts and revenue structures differ; the largest revenue number alone should not decide strategy.

### Team feedback
Confirm the first segment, reviewer source, engineering allocation and payment/contract entity. I will advance product and market work; we will jointly determine technical choices and customization scope.


# 03 Personal-story visual novels


## Page 01 | Executive summary

Help an ordinary person finish a playable personal work, then test purchase, sharing and a second creation.

| Business item | Initial plan |
| --- | --- |
| Customer / payer | Adults with commemorative, school or career stories and rights to use their material |
| Product | Tell the story → confirm characters → generate visuals and branches → complete playable work |
| Free experience | One complete 800–1,200-Chinese-character short work per person, not a paywalled preview |
| Pricing hypothesis | CNY 69 per standard work; free for players |
| Base cohort | 500 visits → 100 completed first works → 12 payers; 15 expected orders |
| 90-day result | Revenue CNY 1,035; full economic result −35,517.80 |

### First recommendation
Deliver ten short works with human assistance. Record generation, review, rework and author experience, then open a controlled 100-person cohort if costs are manageable. The original 30,000–50,000-character concept remains a later quality/cost experiment, not a promise inside the CNY 69 package.

### Decision requested
Agree the first theme, output specification, source rights, generation route and affordable experiment budget. Whether this becomes a frequent-use platform or a commemorative service should depend on actual repeat purchase.


## Page 02 | Customers & the problem

Authors and players are distinct roles. Being moved by a story does not prove willingness to create or pay.

| Role | Demand hypothesis | Behavior to validate |
| --- | --- | --- |
| Author | Wants personal experience turned into a story with choices | Supplies usable material and confirms characters, outline and facts |
| Payer | Purchases a more complete or personalized finished work | Pays after seeing real examples and specifications |
| Player | Enters a friend's story through a link | Starts, reaches an ending and decides whether to create |
| Third party depicted | May have their likeness or experiences used | Required permission, deletion and withdrawal from public sharing |

### Initial segment
Test adult graduation, friendship, career-transition and commemorative stories first. Users need not know scriptwriting or game tools, but must verify people and events. Breakup stories may be researched without claiming therapy or prediction of real people's reactions.

### Behavioral questions
Use a piece of material the user has permission to supply. Observe whether they play through, whom they would show it to, and whether they have another story. Record why people refuse upload or sharing; do not interview only enthusiastic respondents.


## Page 03 | Product & user journey

Confirm source events and invented branches separately before producing a complete playable story.

Start with adults recording graduation, friendship or career transitions. Anniversary gifts are a testable use case; third-party private information without appropriate consent is not a source. Breakup or traumatic experiences may represent demand, but this trial promises neither therapy nor prediction of another person's reactions.

Text or voice input → extract characters, events and chronology → author confirms fact versus fictional branch → generate and approve outline → generate text and images → check reachable branches and character consistency → review where necessary → private work link → author plays through → author chooses whether to share. Before importing chats, remove names, contact details and irrelevant third-party content. Default to private, without training use.

Example: “Turn my transition from leaving a job to winning my first independent contract into a story with three choices.” Confirm which events happened and which alternatives are imagined. AI-written dialogue must not be presented as a real person's original conversation.


## Page 04 | MVP & delivery scope

The free short work must be complete. Paid characters, images, branches and revisions need explicit limits.

Retain the full journey: tell a story → confirm characters → generate visuals and branches → play → share → bring in another author. The first free work is not unfinished content behind a payment wall: plan 800–1,200 Chinese characters across the script, two characters, two scenes, one key choice and two endings. Free visuals use licensed templates; characters follow text descriptions. Paid work can test custom character art based on authorized photos. Photo input belongs to the original ambition, but consistency and permission should first be tested with human-assisted paid work before unreviewed portrait generation is opened.

Keep 30,000–50,000 characters as a later quality/cost experiment, not an included CNY 69 promise. Length alone does not establish story quality or what a player reads. Report total branch-script length separately from estimated time for one route.

Assumed standard paid specification: 3,000–5,000 Chinese characters across branches; at most three main characters; six scene/character assets; three key choices; three endings; one revision round; browser play; 30 days of hosting; and a downloadable local reading package. An estimated 10–20 minutes per route is an assumption to update after testing.


## Page 05 | Market sizing & evidence

The initial market is reachable authors who finish works, not all AI users or all game players.

| Level | Definition | Current state |
| --- | --- | --- |
| TAM | Adults with personal-story demand and permission to provide material | No reliable segment size yet |
| SAM | Chinese short stories, browser play, acceptable template visuals and non-sensitive inputs | Requires interviews |
| Candidate channels | Ten creator/community entries; seek five effective entries | No confirmed partnerships or owned traffic assumed |
| 90-day visits | 500 qualified visits | Depends on real demonstrations and recruitment |
| Activation / sales | 100 complete free works, 12 paid authors, 15 expected orders | Assumes 20% activation, 12% purchase and 25% second purchase |

### Expenditure and capacity
Base additional cash budget: CNY 5,632.80. Total economic expenditure: 36,552.80. Free works have a cost in the model. The first 100 works are a controlled allowance, not an unlimited-free promise.

### Bottom-up method
Attribute deduplicated visits → creation started → playable work finished → purchase → another creation. Track player-sharing traffic separately; work views are not author counts. The broad AI market is context, not a defensible TAM revenue estimate for this product.

Sources: [S1 CNNIC: 2026 generative AI application report](https://www2.cnnic.cn/n4/2026/1008/c326-11703.html)


## Page 06 | Competition & alternatives

The advantage must come from complete production and personal expression, not simply generating more words.

| Alternative | Capability / reference price | Difference to validate |
| --- | --- | --- |
| AI Dungeon | Journey USD 14.99/month; interactive narrative and model allowances | Personal material, consistent characters, a defined finished work and sharing |
| Ren'Py | Open-source visual-novel engine, free for commercial use | Ordinary users avoid learning scripts, asset assembly and branching |
| Writing models + image tools | Users can combine tools themselves | Less switching and rework; a complete experience |
| Human-made commemorative work | High-touch personal expression; actual quotes unverified | Automation reduces cost while preserving personal meaning |

### Comparison task
Use the same authorized personal material with a tool combination and the proposed workflow. Record completion time, learning steps, character errors, image rework, reachable endings and actual willingness to pay.

### If the platform hypothesis fails
If purchases occur mainly on anniversaries, consider a small curated service rather than forcing a high-frequency platform narrative. Completion matters more than total length; a 30,000-character branching script does not mean every player reads 30,000 characters.

Sources: [S8 AI Dungeon official memberships](https://help.aidungeon.com/memberships-benefits); [S9 Ren'Py official website](https://www.renpy.org/)


## Page 07 | Business model & pricing

The author pays for a finished work; players are free. Per-work pricing fits an initial test of potentially infrequent demand.

| Offer hypothesis | Price | Included scope |
| --- | --- | --- |
| First complete short work | CNY 0, once per person | Template visuals, 800–1,200 Chinese characters, two endings and limited hosting |
| Standard work | CNY 69 each | 3,000–5,000 characters, up to three characters, six assets, three endings, one revision |
| Human-polished commemorative edition | CNY 299, capped at the first ten | At most two editing hours; separate specification; price interviews only, excluded from revenue model |
| Long-form / voice / extra branches | Not sold in the initial trial | Quote separately after quality and cost experiments |

The author is the payer; invited players are free. Do not start with an unlimited monthly subscription when demand may occur only on special occasions. Test whether this is a gift business or frequent creation platform. A viable one-time purchase with weak repeat use can support a small service without pretending to be platform growth.

Allow retries for delivery failure. If no playable work is produced within the disclosed waiting period, handle refunds under the stated rules. Budget for retry costs and refund reserves. New characters or a new theme are not unlimited revisions.


## Page 08 | Unit economics & viability

Free-work costs can consume paid contribution. Sharing incentives require a separate budget.

Target full economic cost per free work: CNY 6 = model/template allocation 3 + storage/distribution 1 + review/support 2. Paid work: 18 = text/images 8 + storage/distribution 2 + review/after-sales 8. Add 3% processing and a 5% refund reserve. Direct contribution per paid order = 69 − 18 − 69 × 8% = **CNY 45.48**. Every 100 free works cost 600 and must be included in the funnel economics.

Proposed credit experiment: an author who brings three deduplicated new players who finish playing receives CNY 10 off their next work, at most once per month. No cash withdrawal or stacking. Cap the first trial at 50 credits, CNY 500 face value. This pool is **excluded from the no-incentive base case**. If activated, deduct credits actually redeemed from receipts and track separately. Clicks alone earn no reward. Keep only necessary anti-abuse data.

Illustrative author referral coefficient: 30% share × three unique players per sharer × 10% player-to-author conversion = **0.09**. One hundred authors generate nine new authors on average, far below self-sustaining growth. Holding the first two inputs constant, K > 1 would require more than 100% conversion, which is impossible. More genuine reach or stronger repeat creation is necessary. First measure openings, completed play and willingness to create.


## Page 09 | Acquiring the first customers

Acquire 100 authors who finish their first work, then observe who actually purchases.

Base funnel: **500 qualified visits × 20% completing a first work = 100 activated authors; 100 × 12% purchase = 12 payers.** Assuming 25% buy one additional work within 90 days gives 15 orders. Repeat purchase is an unverified assumption measured over payers, not all players.

Channel targets: five small creators/communities × 50 visits = 250; five playable original examples × 30 = 150; permitted direct invitations and author sharing = 100. Partnerships and follower counts are unconfirmed. Start with ten candidate entries, secure two trials, then deliver in small batches. Demonstrate a playable route rather than only generation videos or polished screenshots.

Cash budget CNY 1,200: samples/assets 500, small collaborations 500, research incentives 200. My 40 hours are valued at 3,200. Base cash CAC is 100 per paid author; including acquisition labor, 366.67. The CNY 69 price and current generation costs do not support paid traffic acquisition at these levels.


## Page 10 | Channels & sales process

Deliver ten samples to test completion and pricing before expanding channels.

| Stage | Action | Evidence |
| --- | --- | --- |
| Sample preparation | Choose two non-sensitive original stories and produce complete routes | Playable and accepted by the author |
| Channel candidates | Identify ten entries; secure two small-trial agreements | Source, agreement and visit attribution |
| Human assistance | Deliver ten short works; record every revision | Cost, completion and user feedback |
| Real quotation | Present the CNY 69 specification for a second/upgraded work | Payment and refunds, not verbal intent |
| Controlled recruitment | After quality/cost gates, admit at most 100 free authors | Activation, completion, sharing and purchase |
| Sharing review | Separate self-testing, friend play and player-to-author conversion | Next-generation authors and their cost |

### Channel content
Share genuinely playable routes, not just screenshots or “generating” footage. State the free specification. Do not attract users with a promised free long story and require payment to reach its ending.

### Original credit mechanism
Test a credit after valid completed play separately, capped at 50 credits and CNY 500 face value. The base model excludes it; deduct actual redemption if used. Credits are not revenue, and the proposal does not use multiple commission levels.


## Page 11 | Financial scenarios

Use the same formula across conservative, base and upside cases. More revenue does not mean total investment is covered.

All amounts in CNY.

| Scenario | 90-day revenue | Direct contribution | Cash expenditure budget | Full economic result |
| --- | --- | --- | --- | --- |
| Conservative | 227.70 | -209.92 | 5,291.22 | -35,809.92 |
| Base | 1,035.00 | 82.20 | 5,632.80 | -35,517.80 |
| Upside | 3,864.00 | 1,346.88 | 7,469.12 | -35,053.12 |


| Input | Conservative | Base | Upside |
| --- | --- | --- | --- |
| Visits / activation | 400 / 15% | 500 / 20% | 800 / 25% |
| Activated authors / purchase | 60 / 5% | 100 / 12% | 200 / 20% |
| Payers / second-purchase probability | 3 / 10% | 12 / 25% | 40 / 40% |
| Expected orders | 3.3 | 15 | 56 |

Base revenue = 15 × 69 = CNY 1,035; direct contribution is only 82.20 after free-work costs. 3.3 orders is a scenario expected value, not an actual order count. Observe a full 90 days after cohort entry; do not assume repeat purchases for late entrants in advance. Additional credits, taxes and unquoted launch costs are excluded.


## Page 12 | Resources & cash planning

Establish whether works can be delivered at target cost before investing in an automated platform.

| Fixed investment | Assumed cost, CNY |
| --- | --- |
| Engineering: 140 hours × 150 | 21,000 |
| Product / narrative: 80 hours × 80 | 6,400 |
| Assets and testing | 2,000 |
| Common hosting: three months × 600 | 1,800 |
| Fixed economic cost | 31,200 |

### Base 90-day budget
Cash 5,632.80; total economic expenditure 36,552.80; revenue 1,035; economic result −35,517.80. Cash assumes internal engineering, narrative and some service labor incur no additional payment; it is not a standalone outsourcing quote.

### Allowances and reserves
100 free works × 6 = 600 full cost. Fifteen paid orders × 18 = 270 direct service cost; processing/refund reserves are additional. If a free work costs 15 rather than 6, expenditure rises by 900 and contribution turns negative. Do not open unlimited free creation expecting sharing to recover the cost.

### Staged approval
Start with ten human-assisted samples. Approve the 100-person allowance only after quality and cost evidence. Set each batch's cap and retry rules. Long stories, voice, repeated polishing and rights purchases are not automatically included.


## Page 13 | 90-day milestones

Separate sample delivery, controlled recruitment and repeat purchases from mature cohorts.

| Checkpoint | Work to complete | Condition for the next step |
| --- | --- | --- |
| D7 | Five interviews; two usable stories and a defined specification | Authors willing to confirm material and characters |
| D14 | Two–three complete short works; present paid scope | Playable from beginning to an ending |
| D30 | Ten human-assisted works delivered | Quality, labor and image retry cost measurable |
| D60 | Open a 100-person cohort only with cost evidence | Actual generation, completion and payment |
| D90 | Observe mature-cohort repeat purchase and sharing-led creation | Choose platform, service or stop |

### Observation window
The financial 90 days run from author cohort entry. Late entrants are not credited with future second purchases or classified as due churn. One hundred authors are not 100 active paying users.

### Joint engineering assessment
Start with an assisted workflow if appropriate; build a web task queue after sample validation if justified. Select engine, text/image models, hosting and export format with the team based on quality, cost and effort.


## Page 14 | Metrics & acceptance criteria

Complete works, author approval, player completion and actual purchase each need their own denominator.

In the first ten human-assisted works, record actual labor minutes, generation count, image rework and reasons for edits. Acceptance requires every choice to reach an ending, no dead links, consistent names and relationships, clear fact/fiction separation, author deletion and sharing withdrawal, and mobile play from beginning to at least one ending. Authors must approve visual consistency; model output is not automatically acceptable.

Suggested continuation gates: at least seven of the first ten authors approve characters/story; at least five play through without further explanation. In the 100-person batch, generation completion ≥80%, first-route completion ≥50%, sharing ≥25%, standard paid conversion ≥12%, and zero serious privacy incidents. Actual retry-inclusive cost must remain within the price-supported limit. If works look good but users do not play/share, test gift or commemorative demand. If free costs cannot be controlled, close open recruitment and retain only limited trials.

### Repeat and sharing definitions
Second purchasers / paying authors with the relevant completed observation window. Player-to-author conversions / unique shared-link players. Remove author self-tests and duplicate accounts; report incentive cohorts separately. Link clicks are not completed play.


## Page 15 | Risks & responses

Story quality, generation cost and rights to personal material determine whether the service can continue.

| Risk | Early signal | Response / responsibility |
| --- | --- | --- |
| Incomplete work | Dead branches, missing endings or assets | Engineering validates reachability; no unfinished delivery |
| Inconsistent characters | Names, relationships or images change | I design confirmation steps; author accepts the work |
| Cost escalation | Image retries, long expansion, unlimited editing | Cap scope and revisions; quote additions |
| Privacy / rights | Unapproved photos, chats or third-party material | Private by default; de-identify and confirm permission; sharing can be withdrawn |
| Sharing fails to convert | Views without new authors | Diagnose creation friction; views are not growth |
| Infrequent demand | Occasion-only purchases and little repeat use | Consider per-work gift service rather than monthly subscription |

### Fact and fiction
AI-added dialogue and alternative-choice scenes must be identified as creative material, not real chats, real reactions or predictions of a life. Preserve generation labels in the experience and export.

### Stop conditions
Pause open recruitment if generation cost consistently exceeds what price supports, source rights cannot be explained, or a serious privacy issue occurs. Address causes and affected works first.

Sources: [S12 Measures for labeling AI-generated synthetic content](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)


## Page 16 | Team roles & collaboration

I will lead product and market execution, while assessing technical choices and resources jointly with the team.

### My proposed responsibilities
I will own character and narrative experience, work specifications, author recruitment and sample delivery. I can rapidly prototype and prepare experiments with AI, and want to assess reliability, costs and scalable implementation with engineering. A prototype is not proof of production-service readiness.

| Role | Proposed responsibility | To confirm |
| --- | --- | --- |
| 最高 | Product, customers/users, market work, experiments and review | Availability and stage targets |
| Engineering lead | Architecture, models/tools, permissions, tasks and cost logs | People, hours, schedule and maintenance |
| Professional / content reviewer | Facts, asset rights and output quality | Reviewer, competence, price and scope |
| Customer / user | Usable material, confirmation, feedback and acceptance | Consent and intended use |
| Team247 lead | Budget, resources, payment/contract entity and stage decisions | Authority and available resources |

### Decisions to make together
Launch platform, core tasks, models/tools, usage budget, data handling, release requirements, price, responsibilities and acceptance. Joint discussion is not an excuse to provide no proposal: this BP offers comparable assumptions and experiments for the team to revise.

### Working cadence
Review real activations/customers, payments/refunds, output quality, effort/API costs and next-week decisions weekly. Record a continue/adjust/pause decision at days 14 and 30. These are proposals, not staffing or budget commitments already obtained.


## Page 17 | Evidence, assumptions & unknowns

Public sources support context and constraints. Project revenue and growth remain unverified assumptions.

| Evidence | Date and limits |
| --- | --- |
| [S1 · CNNIC: 2026 generative AI application report](https://www2.cnnic.cn/n4/2026/1008/c326-11703.html) | Published 2026-10-08; first half of 2026. Official indexed summary only; direct body retrieval timed out. More than 700 million AI users is context, not the size of this paying segment. |
| [S8 · AI Dungeon official memberships](https://help.aidungeon.com/memberships-benefits) | Dynamic page; checked 2026-11-09. Journey USD 14.99/month and tiered plans. This does not validate local pricing for personal visual novels. |
| [S9 · Ren'Py official website](https://www.renpy.org/) | Dynamic page; checked 2026-11-09. Open-source visual-novel engine, free for commercial use. Other assets and production do not become free. |
| [S12 · Measures for labeling AI-generated synthetic content](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm) | Published March 2025; effective 2025-09-01. Explicit and implicit labeling requirements. This does not mean any required filing or approval has been completed. |

### Critical gaps
Real author demand; generation retries and review time; paid/repeat purchase; sharing-to-creation conversion; rights to character material; cost of the first free work.

### Replace assumptions with evidence
Use sourced prospect records, interviews, payment/refund records, task logs, supplier invoices and mature-cohort observations. Mark missing evidence as unverified; do not invent customers, case-study revenue, permissions or testimonials.

### Evidence levels
Public facts retain their sources and dates. Prices, counts and costs are planning assumptions. Formula outputs are calculations. Relationships, resources and technical capability remain to be validated. Recheck dynamic prices before launch. The BP and website are deliverables; commercial viability has not been established.

Sources: [S1 CNNIC: 2026 generative AI application report](https://www2.cnnic.cn/n4/2026/1008/c326-11703.html); [S8 AI Dungeon official memberships](https://help.aidungeon.com/memberships-benefits); [S9 Ren'Py official website](https://www.renpy.org/); [S12 Measures for labeling AI-generated synthetic content](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm)


## Page 18 | Recommendation & decisions

Use ten complete samples to validate author value before choosing a creation platform or a per-work commemorative service.

| Decision | Proposed starting point |
| --- | --- |
| First context | Adult graduation, friendship or career-transition stories |
| Samples | Ten human-assisted complete short works; record effort and rework |
| Price | One limited complete work free; standard work at an assumed CNY 69 |
| Next target | A 100-author trial after quality gates; observe purchase, sharing and repeat use |
| Continue when | Authors approve, routes work, cost is controlled and payments occur |
| Pause when | Low completion, uncontrolled free cost or unresolved rights/privacy |

### Why retain the direction
It fits narrative and visual capabilities and produces a demonstrable finished experience. Demand may be infrequent, however, and free creation/sharing do not automatically yield sustainable growth. Let use and purchase determine the format.

### Comparison with the other directions
Personal AI focuses on frequent tasks and long-term user scale. The industry agent focuses on defined business delivery. Stories focus on personal works and sharing. All are discussable, but three complete development budgets should not be presumed approved together.

### Team feedback
Confirm first-work specification, automation level, review and asset-rights rules, trial budget and engineering support. Choose engine and models jointly after comparing sample quality and cost.


# Comparison & priorities

Agree the review objective before prioritizing resources. Near-term paid delivery and a scalable consumer strategy require different decisions.


| Dimension | Personal AI | Industry agent | Personal-story visual novels |
| --- | --- | --- | --- |
| Product | Everyday personal AI assistant | Professional workflow with bounded delivery | Creation and play of personal works |
| Payer | Individual user | Institution / brand budget owner | Author |
| Price hypothesis | CNY 1/month; 10/month; or first month 1 then 10 | 2,980 pilot; 1,980/month | First work free; 69/standard work |
| Scale objective | 1,000 → 10,000 → 100,000 activated users | First ten paid pilots, then a repeatable prospect pool | Ten samples, then 100 authors |
| Validation focus | Usefulness, retention, referral K, unit cost | Payment, factual quality, total effort, renewal | Completion, approval, purchase, sharing |
| Key dependencies | Model/tool costs, system capabilities, reward rules, channels | Professional material, review, customer access | Narrative quality, asset rights, generation cost |

### Recommended discussion order
**For a mass-market, scalable product strategy, discuss personal AI first.** I bring the ambition and growth model; the team jointly selects tasks, engineering, pricing and investment. Assess it as a useful personal assistant rather than only a reminder, while keeping the 100,000-user target separate from actual evidence.

**For the fastest test of a bounded paid service, pilot the industry agent first.** Its payer and task are more specific, but scalability as a subscription platform remains unproven.

**Keep personal stories as a separate product experiment.** Validate value through limited samples. If repeat demand is weak, per-work service may be appropriate rather than a high-frequency platform.

### Limits on financial comparability
The updated personal-AI tables model first-month and 90-day cohorts at different scales, excluding common construction. Industry and story tables cover 90-day trials including construction. Their result figures cannot directly rank profitability. Pages 11–12 define each period, cost scope and unknown.

### Resource decision
Do not assume all three full builds launch at once. First select consumer-scale exploration or near-term paid-delivery validation, then assign a lead direction, owner, budget and review gates. The prior ranking emphasized cash validation; this version incorporates the broader ambition.



# Responses to the review requests

A substantive response to the feedback supplied by 最高, with direct links to the relevant pages. Private chat screenshots are not reproduced.


### R1 — Market, reach, expenditure, assumptions and sources
Each proposal separates broad context, a serviceable segment and actual reachable prospects. Personal AI targets 1,000 / 10,000 / 100,000 activations; the industry plan builds a 200-prospect list toward ten pilots; stories use 500 visits toward 100 complete works. Conversion and expenditure figures are hypotheses. Unknown TAM/SAM is marked explicitly; all AI users or all hospitals are not substituted for the relevant market.

See each project's **page 05 market, 11 finance, 12 resources and 17 evidence**. Direct links are provided below.

### R2 — Payer, price, frequency and delivery
Personal AI charges the user monthly, comparing CNY 1, 10, and first month 1 then 10. The one-time CNY 1 direct-referral reward is a growth experiment with service and reward costs calculated. Industry customers pay 2,980 per pilot or 1,980/month. Story authors pay 69/work; players are free. All proposals specify delivery and allowance limits.

See **page 04 scope, 07 pricing and 08 unit economics**.

### R3 — Acquiring the first ten customers or 100 users
These are early feedback checkpoints, not growth ceilings. Personal AI starts with 100–200 seed users, pursues 1,000 activations, then progresses toward 10,000 and 100,000 using evidence. Industry and story proposals provide sources, staged funnels, workload and cash budgets.

See **page 09 acquisition, 10 channels/growth and 13 milestones**. Personal-AI page 10 explains the CNY 1 referral mechanism and K.

### R4 — What to test first and why
For a consumer-scale strategy, prioritize discussing personal AI. For short-term bounded paid delivery, start with the industry agent. For stories, first validate ten complete samples. A single ranking based only on small-cohort cash validation does not express the updated strategic objective. Each proposal includes evidence that can change the decision and conditions to pause.

See **Comparison**, plus each project's **page 14 validation and 18 decisions**.

### R5 — Concrete numbers for a comprehensive review
Provide a common 18-page structure, evidence categories, six relevant industry/story financial cases and nine updated personal-AI cases: three scales × three prices. Inputs and scripts are downloadable. Cost and period differences remain explicit to prevent false comparisons.

### The collaboration position
I want to bring a worthwhile product ambition, a discussable growth model and an explicit validation path, while leading product, market work and execution. I want technical choices, prices, resources and implementation to be assessed jointly with the team. This BP supplies the analysis needed for that discussion without deciding engineering unilaterally.



# Definitions, data & attachments

These are plans and models for joint decisions, not evidence of actual customers, payments, permissions or committed staffing.


### Four evidence categories
**Public fact:** an original source and date. **Planning assumption:** prices, counts, conversion, hours and budgets. **Calculated result:** a formula applied to assumptions. **To validate:** relationships, channels, technology, rights and team resources.

### Financial definitions
Amounts are in Chinese yuan (CNY) unless USD is explicitly stated. Gross revenue is not cash collected or profit. Direct contribution deducts service and specified channel/loss reserves. Full economic results then account for acquisition, fixed costs and labor. Unquoted taxes, release requirements, additional asset licenses and actual store commissions cannot be presumed zero.

### Version history
The current BP uses the broad personal-AI positioning and CNY 1/10 models. V5's CNY 29 character assistant, 100-person target and earlier priority ranking are retained only as historical research and superseded for personal AI. The industry and story research continues to support the current proposals.

### Attachments
Download Prompt V2.1, all current pages, the new personal-AI growth model and reproduction script, industry/story scenarios, and clearly labeled historical research. Historical Chinese originals retain their original language and are not current personal-AI proposals.

### Actual execution status
This work delivers the proposals, models and static reading website. No external messages, advertising, contracts, payments or referral rewards have been executed. Technical selections and resourcing remain joint team decisions.
