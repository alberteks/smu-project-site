# Survey Data Analysis

## Methods

An electronic survey\* was distributed to all upper school students in Eastside Preparatory School (Kirkland, WA) and Lakeside School (Seattle, WA) in the Spring of 2026\. Data tracing students to specific schools was not recorded, although roughly equal participation from both schools is assumed. Participation was voluntary and completely anonymous. 

\*Thank you to PEW Research Center for inspiration on a number of basic survey questions.

The raw dataset contains 182 total responses. Three responses were discarded due to clear non-serious entries, leaving a sample of N = 179. Of these, 156 students (approximately 87.2%) reported using social media on at least a “semi-regular basis” and 23 (approximately 12.8%) reported that they do not. Non-users answered a separate question set, therefore most of the data analyses were centered around the 156 users’ responses. 

Those who self-identified as female were slightly better represented in the sample (N = 179): 94 female, 67 male, 11 prefer not to say, 6 non-binary, and 1 other. Participation was roughly balanced across grade levels: 49 participants indicated they were freshmen, 47 sophomores, 42 juniors, and 41 seniors. Among the 156 users, the breakdown was as follows: 82 female, 59 male, 11 prefer not to say, 3 non-binary, 1 other; 41 freshmen, 38 sophomores, 37 juniors, and 40 seniors.

Text-based ordinal responses were mapped to numerical scales for comparative testing. Ranges under ‘time spent’ were interpreted as follows: “Less than 1 hour” = 0.5, “1-2 hours” = 1.5, … “6+ hours” = 6.5. Many questions in the survey consisted of frequency scales which were also quantified for data analysis (“Not at all”/“Never” = 0, “Rarely” = 1, “Sometimes” = 2, “Often” = 3, “All the time” = 4). For overall effect: “Mostly negative” = -1, “Neither positive nor negative” = 0, “Mostly positive” = +1. For feelings: “No” = 0, “Yes, a little” = 1, “Yes, a lot” = 2.

Claude Opus 5 was used to aid with data analysis without interpretation; figures were then manually vetted to ensure accuracy. Statistical analysis was conducted in Python (pandas 3.0.5, SciPy 1.18.0). Spearman rank-order correlation was used to measure the strength and direction of associations between ranked or ordinal variables. A Mann-Whitney U test with a rank-biserial correlation as the effect size was used to compare ordinal outcomes between groups. A Kruskal-Wallis H test with ε² as the effect size was used to determine whether ordinal distributions vary across three or more groups. A chi-square test of independence with Cramér’s V was used to gauge relationships between categorical variables. Fisher’s exact test was used when there were few expected cell counts.

Approximately 130 statistical tests were conducted for the dataset at a 5% error rate ($\alpha =0.05$). At this threshold, about 6 or 7 results would be expected to appear “significant” due to chance alone. To mitigate this, every p-value reported was run through a Benjamini-Hochberg false-discovery-rate-adjusted q-value: if a result makes it through the correction, it is treated as significant. The precision of each proportion estimate is reported with 95% Wilson confidence intervals.

Three robustness checks were done. The hours variable was re-coded in four different ways: top band as 6.5, 7.5, 6.0, and pure rank order, and given that Spearman correlation works with ranks, none of the coefficients changed. Upon re-running the headline correlations, (including the three responses that were excluded) none changed by more than 0.06. Finally, an assessment of the internal consistencies of three composite scales used was conducted: Cronbach’s $\alpha =0.784$ for the six-item negative-habit composite, 0.720 for the four-item positive-feelings scale, and 0.711 for the four-item negative-feelings scale, which are all acceptable.

## **Results by Data Category**

**Category I: Social Media Use & Sleep**

* Using social media within one hour of going to bed and going to sleep later than planned were significantly associated with one another (ρ = 0.596, 95% CI \[0.48, 0.69\], p = 2.3 × 10⁻¹⁶, q &lt; 0.0001, n = 156.) Total daily hours of sleep lost and daily average hours of social media usage were also correlated (ρ = 0.511, 95% CI \[0.38, 0.62\], q &lt; 0.0001).  
* 72.4% of students (113/156, 95% CI \[64.9, 78.8\]) self-report using social media within one hour of going to bed “often” or “all the time,” and only 2 students report never doing so. 39.7% (62/156, 95% CI \[32.4, 47.6\]) of students self-report that social media causes them to go to sleep later than planned “often” or “all the time.”

**Category II: Time Spent on Social Media & Academic Procrastination**

* Daily average hours of social media usage and using social media to “consciously put off tasks” are moderately correlated: ρ = 0.452, 95% CI \[0.31, 0.58\], p = 3.1 × 10⁻⁹, q &lt; 0.0001. Procrastination and distraction while “actively working on school-related tasks” were also correlated (ρ = 0.491, q &lt; 0.0001), along with decreased sleep time and procrastination (ρ = 0.490, q &lt; 0.0001).   
* 49.4% (77/156, 95% CI \[41.6, 57.1\]) of students self-report using social media to put off tasks “often” or “all the time.” Additionally, 76.9% (120/156) self-report being distracted while doing schoolwork at least “sometimes,” and only 5.8% (9 students) report never being distracted by social media while doing schoolwork.

**Category III: Impact of Social Media Use on Teens in Different Age Groups**

* 9th graders in this sample were more likely than 12th graders to self-report that social media has a “mostly negative” personal effect on them. When 9th and 12th graders are compared, the results are as follows: χ² = 10.98, df = 2, p = 0.0041, Cramér's V = 0.368, n = 81; Fisher's exact test on the "mostly negative" split alone gives OR = 4.04, p = 0.0037. Time spent does not differ from grade-to-grade (Kruskal–Wallis H = 0.969, p = 0.809).  
* Trends do not become more or less pronounced as grade levels rise. 9th graders emerged as an outlier while grades 10 through 12 were more similar to each other, with confidence intervals nearly fully overlapping. Testing for broader trends across levels did not yield any significant results ($\rho =0.174$, $q=0.166$). 

| Grade | n | “Mostly negative” about self | 95% CI |
| :---- | :---- | :---- | :---- |
| Freshman (9th) | 41 | 26 (63.4%) | \[48.1, 76.4\] |
| Sophomore (10th) | 38 | 14 (36.8%) | \[23.4, 52.7\] |
| Junior (11th) | 37 | 14 (37.8%) | \[24.1, 53.9\] |
| Senior (12th) | 40 | 12 (30.0%) | \[18.1, 45.4\] |

* Any differences in behavior between 9th graders and other grade levels were not statistically significant. Eleven outcomes were tested across grade levels: daily hours spent on social media, all six habit measures, both feelings composites, and self-rated effect. None survived correction (all $q>0.40,\ {\varepsilon }^{2}\leq 0.047$). 9th graders do not report using social media more, scrolling in bed more, losing more sleep, procrastinating more, or experiencing more negative feelings than 12th graders.  
* 9th and 12th graders were essentially equally likely to perceive social media’s effect on *people their age* as “mostly negative,” with 78.0% of 9th graders and 80.0% of seniors responding as so (grade$\times$peer effect: ${\chi }^{2}=7.69,\ p=0.2614$). Freshmen only differed on how they perceived social media’s effect on themselves. 

**Category IV: Role of Gender in Mediating Social Media \- Mental Health Associations**

* Comparing female (n = 82) and male (n = 59) users across eleven outcomes, with FDR correction applied:

| Outcome | Mean F | Mean M | r\_rb | p | q (FDR) |  |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| Negative-feelings score (0-8) | 1.93 | 0.92 | \+0.338 | 0.0004 | 0.0044 | significant |
| Bedtime use | 3.17 | 2.75 | \+0.262 | 0.0050 | 0.0272 | significant |
| Sleeping later than planned | 2.40 | 1.92 | \+0.241 | 0.0118 | 0.0432 | significant |
| Positive-feelings score (0-8) | 3.45 | 2.73 | \+0.212 | 0.0302 | 0.0830 | ns |
| Morning scroll | 2.17 | 1.78 | \+0.172 | 0.0749 | 0.1584 | ns |
| Procrastination | 2.60 | 2.29 | \+0.163 | 0.0864 | 0.1584 | ns |
| Lurking | 1.85 | 1.61 | \+0.115 | 0.2315 | 0.3145 | ns |
| Effect on self | \-0.15 | \-0.31 | \+0.115 | 0.2110 | 0.3145 | ns |
| Hours per day | 2.11 | 1.94 | \+0.106 | 0.2573 | 0.3145 | ns |
| Distracted during schoolwork | 2.35 | 2.19 | \+0.093 | 0.3256 | 0.3581 | ns |
| Social media over in-person time | 1.41 | 1.31 | \+0.071 | 0.4437 | 0.4437 | ns |

The most conspicuous differences were in the eight-item feelings battery. With correction applied across the eight: 

| Item | Female | Male | r\_rb | q |
| :---- | :---- | :---- | :---- | :---- |
| Feel worse about own life compared to others | 54% | 31% | \+0.243 | 0.0128 |
| Feel pressure to post content that gets likes | 39% | 17% | \+0.218 | 0.0128 |
| Feel overwhelmed by drama | 29% | 10% | \+0.192 | 0.0128 |
| Feel friends are leaving them out | 44% | 24% | \+0.206 | 0.0206 |
| Feel more connected to friends’ lives (*positive*) | 85% | 73% | \+0.267 | 0.0128 |
| Feel they have a creative outlet (*positive*) | 72% | 49% | \+0.214 | 0.0266 |

All six items survive correction. The social-comparison item regarding feeling worse about one’s own life compared to others shows the widest gap and is the closest measure in this survey to body-image and social-comparison findings described in literature. 

**Additional Statistical Trends: Time Spent and Perceived Personal Effect**

* There is a weak negative association between daily average hours of social media usage and how students rate social media’s effect on them personally ($\rho =-0.191,$ 95% CI \[-0.35, \-0.03\], p = 0.0170, q = 0.029). Students who self-report more hours of social media use are somewhat more likely to rate the effect social media has on them as “mostly negative.” However, this relationship is tenuous since it only accounts for around 3.6% of the variance; furthermore, partial correlation analysis indicates that it is not independent of what students do during those hours on social media:

| Controlling for | Partial $\rho$ | p |  |
| :---- | :---- | :---- | :---- |
| (*nothing — raw*) | \-0.191 | 0.017 |  |
| Sleeping later than planned | \-0.076 | 0.349 | drops out |
| All four behavior habits | \-0.095 | 0.244 | drops out |
| Procrastination | \-0.180 | 0.025 | holds |
| Negative-feelings score | \-0.172 | 0.033 | holds |

Of the 66 pairwise correlations tested, 42 survive FDR correction. The strongest links, all q &lt; 0.0001 are as follows:

* Bedtime use $\times$ sleeping later: $\rho =0.596$  
* Hours $\times$ bedtime use: $\rho =0.544$    
* Hours $\times$ sleeping later: $\rho =0.511$    
* Distraction $\times$ procrastination: $\rho =0.491$    
* Sleeping later $\times$ procrastination: $\rho =0.490$    
* Hours $\times$ morning scroll: $\rho =0.483$    

Of the 66 correlations, 3 are large ($\left|{\rho }\right|\geq 0.50$), 17 moderate (0.30-0.50), 30 small (0.10-0.30), and 16 negligible. Habits tended to cluster; in other words, students who reported one tended to also report the others. 

The habit most associated with negative feeling is displacement of in-person time; in other words, opting to go on social media rather than engaging with one’s friends or family in-person. It correlates with the negative-feelings score at $\rho =0.379,$ q &lt; 0.0001.

**Notable Non-Significant Trends:**

* Grade level does not predict screen time (H = 0.969, p = 0.809); 9th and 12th graders report nearly identical usage.  
* Gender does not predict screen time (p = 0.257) or lurking (p = 0.232)  
* Daily hours are not associated with any of the eight feelings items after correction (all $q\geq 0.0997$)  
* Primary social media platform used does not predict habit intensity (H = 4.777, p = 0.311)  
* Posting status does not significantly predict perceived personal effect (${\chi }^{2}=3.648,$ p = 0.161)

**What Students Report Experiencing:** 

The survey contained eight questions about how social media makes students feel: four were framed positively and four negatively. This was the closest way of measuring students’ well being in our survey. Results were the most balanced in our dataset:

| Item (Social media makes you feel…) | No | A little | A lot | Any | 95% CI |
| :---- | :---- | :---- | :---- | :---- | :---- |
| More connected to friends’ lives (+) | 32 | 60 | 64 | 79.5% | \[72, 85\] |
| A place to show your creative side (+) | 56 | 64 | 36 | 64.1% | \[56, 71\] |
| More accepted (+) | 77 | 59 | 20 | 50.6% | \[43, 58\] |
| People who support you through tough times (+)  | 89 | 47 | 20 | 42.9% | \[35, 51\] |
| Worse about your life compared to others (-) | 88 | 54 | 14 | 43.6% | \[36, 51\] |
| Friends are leaving you out of things (-) | 101 | 47 | 8 | 35.3% | \[28, 43\] |
| Pressure to post content that gets likes (-) | 109 | 38 | 9 | 30.1% | \[23, 38\] |
| Overwhelmed by all the drama (-) | 121 | 27 | 8 | 22.4% | \[17, 30\] |

* Positive experiences are reported more often than negative ones. The positive-feelings score averages 3.27 against 1.56 for negative feelings (Wilcoxon signed-rank, $p=6.3\times 1{0}^{-12}$) on the 0-8 composite scales. 104 students score higher on positive than negative, 26 the reverse, and 26 are tied. 

Daily average hours of social media usage does not predict how students feel. Each of the eight items was correlated against daily hours, with correction applied:

| Item (Social media makes you feel…) | $\rho$ with hours/day | q |  |
| :---- | :---- | :---- | :---- |
| Worse about own life vs others | \+0.184 | 0.0997 | ns |
| Connected to friends’ lives | \+0.170 | 0.0997 | ns |
| Creative outlet | \+0.167 | 0.0997 | ns |
| More accepted | \+0.141 | 0.1601 | ns |
| People who support them | \+0.128 | 0.1796 | ns |
| Pressure to post for likes | \+0.086 | 0.3806 | ns |
| Overwhelmed by drama | \+0.070 | 0.3860 | ns |
| Friends leaving them out | \+0.070 | 0.3886 | ns |

* For time spent, none survives correction. Daily average hours of social media usage predict behavior (e.g., bedtime or procrastination) much better than feelings.  
* Students who self-reported feeling worse about their own lives compared to others on social media were more likely to rate social media negatively for themselves ($\rho =-0.218,\ q=0.025$). This was also the case for students self-reporting personally feeling no connection, support, or acceptance on social media ($\rho =+0.228,\ +0.196,\ +0.192{\ }$ respectively, all $q<0.05$). Of the three other negative items (drama, posting pressure, feeling left out), none were found to be associated with overall self-rating after correction was applied.

**Platform Specifics & Habits** 

Among the 156 students who report using social media platforms on “at least a semi-regular basis,” platform of choice is fairly concentrated. The platform breakdown is as follows (multi-select multiple choice answers, so totals exceed 100%): 

| Platform | n | % of users | 95% CI |
| :---- | :---- | :---- | :---- |
| Instagram | 113 | 72.4% | \[64.9, 78.8\] |
| YouTube (Shorts) | 75 | 48.1% | \[40.4, 55.9\] |
| Snapchat | 44 | 28.2% | \[21.7, 35.7\] |
| TikTok | 42 | 26.9% | \[20.6, 34.4\] |
| Reddit | 23 | 14.7% | \[10.0, 21.2\] |
| Other | 22 | 14.1% | \[9.5, 20.4\] |
| X (Twitter) | 8 | 5.1% | \[2.6, 9.8\] |
| Facebook | 2 | 1.3% | \[0.4, 4.6\] |

By most-used platform: Instagram 75, YouTube Shorts 34, TikTok 25, Other 10, Snapchat 6, Reddit 3, X (Twitter) 3, Facebook 0\.

Scoring each student’s six habit measures on the 0-4 scale gives a composite out of 24; ranked by that score:

| Primary platform | n | Habit score /24 | 95% CI | Mean hours/day |
| :---- | :---- | :---- | :---- | :---- |
| X (Twitter) | 3 | 18.33 | \[12.1, 24.6\] | 3.50 |
| Instagram | 75 | 13.69 | \[12.8, 14.6\] | 2.06 |
| TikTok | 25 | 13.20 | \[11.2, 15.2\] | 2.38 |
| Other | 10 | 12.90 | \[8.5, 17.3\] | 3.10 |
| YouTube Shorts | 34 | 12.56 | \[11.4, 13.7\] | 1.68 |
| Snapchat | 6 | 10.00 | \[4.9, 15.1\] | 1.00 |
| Reddit | 3 | 9.67 | \[5.1, 14.2\] | 2.17 |

* Upon statistical analysis, these differences are not statistically distinguishable from pure chance. Across the five platforms with $n\geq 6$: Kruskal-Wallis H$=4.777,\ p=0.3109,\ {\varepsilon }^{2}=0.032$; primary platform accounts for around 3% of the difference in habit score. Instagram (n = 75) against YouTube Shorts (n = 34) yields p = 0.0916.  
* Variety in habit score may, however, be explained by time spent rather than the specific platform. Adjusting the habit score for daily hours removes it (H = 5.822, p = 0.2128). Students who self-reported Instagram as their most-used platform report, on average, spending more time on social media than those who self-reported YouTube Shorts as their most-used platform (2.06 vs. 1.68 hours), and trends in their habits track as well. Specific habit rates by platform are as follows:

| Platform | n | Bedtime scrolling (often/all the time) | 95% CI |
| :---- | :---- | :---- | :---- |
| X (Twitter) | 3 | 100.0% | \[43.8, 100\] |
| Instagram | 75 | 80.0% | \[69.6, 87.5\] |
| TikTok | 25 | 72.0% | \[52.4, 85.7\] |
| YouTube Shorts | 34 | 67.6% | \[50.8, 80.9\] |
| Snapchat | 6 | 50.0% | \[18.8, 81.2\] |
| Other | 10 | 50.0% | \[23.7, 76.3\] |
| Reddit | 3 | 33.3% | \[6.1, 79.2\] |

Every interval overlaps every other interval. This is also the case for scrolling in the morning (TikTok 52.0%, Instagram 45.3%, YouTube Shorts 11.8%) and procrastination (Instagram 52.0%, YouTube Shorts 47.1%, TikTok 44.0%)

Across all 156 users, the proportion reporting each behavior “often” or “all the time” is as follows:

| Habit | n | % | 95% CI | Mean (0-4) |
| :---- | :---- | :---- | :---- | :---- |
| Using social media within 1 hour of bed | 113 | 72.4% | \[64.9, 78.8\] | 2.96 |
| Using social media to consciously put off tasks | 77 | 49.4% | \[41.6, 57.1\] | 2.46 |
| Distracted during schoolwork | 63 | 40.4% | \[33.0, 48.2\] | 2.24 |
| Going to sleep later than planned | 62 | 39.7% | \[32.4, 47.6\] | 2.16 |
| Scrolling within 1 hour of waking | 60 | 38.5% | \[31.2, 46.3\] | 2.02 |
| Lurking  | 44 | 28.2% | \[21.7, 35.7\] | 1.78 |
| Choosing social media over in-person time | 13 | 8.3% | \[4.9, 13.7\] | 1.35 |

* Evening use is by far the most common habit while displacing in-person interaction with social media is by far the least.

There was a large gap between how students assessed social media’s overall effect on themselves compared to people their age. 

|  | Mostly negative | Neither | Mostly positive |
| :---- | :---- | :---- | :---- |
| Effect on *people my age* | 113 (72.4%) | 38 (24.4%) | 5 (3.2%) |
| Effect on *me personally* | 66 (42.3%) | 57 (36.5%) | 33 (21.2%) |

* 67 students indicated their belief of social media affecting people their age worse than themselves; only 6 rated people their age as better off (Wilcoxon signed-rank, $p=5.1\times 1{0}^{-12}$). Self and peer ratings are correlated ($\rho =0.423,\ q<0.0001$).   
  \[Discussion: This is consistent with the third-person effect of judging the media’s effect on others harsher than they would otherwise on themselves. This phenomenon indicates that if students believe others are more affected by social media than them, the 42.3% personal-harm figure is more likely to be a floor.\]  
* Those who self-report not using any social media platforms on a semi-regular basis tend to exhibit very similar views of social media’s impact on people their age (78.3% vs. 72.4% “mostly negative,” Fisher p = 0.6248), and grade level makes no difference to projection onto peers (p = 0.2614).

Of the 156 students who reported using social media on at least a “semi-regular basis,” 93 report that they post content and 63 report that they use social media (or “lurk”) without posting.

* Those who self-report not posting on social media were more likely to rate social media’s personal effect on them as ‘mostly negative’: 50.8% (32/63, CI \[39, 63\]) compared to 36.6% (34/93, 95% CI \[27, 47\]) for posters. However, this difference is not statistically significant (${\chi }^{2}=3.648,\ df=2,\ p=0.1614,$ Cramér's V = 0.153; Fisher’s exact on the negative split alone: OR = 0.56, $p=0.0987$), and the confidence intervals significantly overlap.

On the other hand, posting may bidirectionally predict the intensity of experience: 

| Outcome | Posters | Non-posters | r\_rb | Q (FDR) |  |
| :---- | :---- | :---- | :---- | :---- | :---- |
| Positive-feelings score (0-8) | 4.01 | 2.17 | \+0.512 | &lt;0.0001 | significant |
| Morning scroll | 2.41 | 1.44 | \+0.412 | &lt;0.0001 | significant |
| Negative-feelings score (0-8) | 1.81 | 1.21 | \+0.226 | 0.0481 | significant |
| Hours per day | 2.30 | 1.77 | \+0.207 | 0.0589 | ns |
| Bedtime use | 3.05 | 2.83 | \+0.167 | 0.1378 | ns |
| Sleeping later than planned | 2.20 | 2.10 | \+0.048 | 0.6585 | ns |
| Distracted during schoolwork | 2.25 | 2.22 | \+0.013 | 0.8848 | ns |

* The difference in positive feelings (r\_rb = +0.512) is the largest group difference in this dataset. Students who post on social media report experiencing more benefits like being able to show their creative side, connecting with friends, and feeling supported or accepted. They do, however, also report experiencing somewhat more of the costs of using social media. They do not report worse impacts on sleep, more distraction, or increased procrastination due to social media.

The 93 students who post tend to post things that could be perceived as more presentable rather than vulnerable:

| Topic | n | % of posters | 95% CI |
| :---- | :---- | :---- | :---- |
| Your accomplishments | 49 | 52.7% | \[42.6, 62.5\] |
| Your family | 38 | 40.9% | \[31.4, 51.0\] |
| Your political beliefs | 29 | 31.2% | \[22.7, 41.2\] |
| Your emotions and feelings | 17 | 18.3% | \[11.7, 27.3\] |
| Your dating life | 15 | 16.1% | \[10.0, 24.9\] |
| Personal problems you’re having | 11 | 11.8% | \[6.7, 20.0\] |
| Your religious beliefs | 9 | 9.7% | \[5.2, 17.4\] |

* Students self-report posting about their accomplishments around 4.5 times more often than their personal problems.

Among the 66 students who indicated that social media had a “mostly negative” impact on them, the following reasons were given:

| Reason | n | % | 95% CI |
| :---- | :---- | :---- | :---- |
| Concerns about the amount of time spent | 62 | 93.9% | \[85.4, 97.6\] |
| Potential negative effects on mental health | 33 | 50.0% | \[38.3, 61.7\] |
| Things seen can be fake or unrealistic | 29 | 43.9% | \[32.6, 55.9\] |
| Drama or negativity | 22 | 33.3% | \[23.2, 45.3\] |
| Data privacy / targeted advertisement concerns | 20 | 30.3% | \[20.6, 42.2\] |
| Unsure / just because it does | 7 | 10.6% | \[5.2, 20.3\] |

* Concerns about time spent on social media is overwhelmingly the most common concern.  
* For the 33 students who indicated social media’s impact on themselves as “mostly positive,” the most popular reasons were information and learning (87.9%), connections and socializing (81.8%), and entertainment and fun (81.8%). Significantly fewer attributed it to wellbeing benefits (15.2%).  
* 78.2% of students (122/156) report viewing posts, stories, or profiles without letting anyone know to at least some degree; 28.2% (44 students, 95% CI \[21.7, 35.7\]) self-report doing so “often” or “all the time,” while only 34 report never doing it.  
* Lurking does not correlate in any way with gender (p = 0.232) or how students rate social media’s effect on them ($\rho =-0.027$, p = 0.738). It very slightly correlates with sleeping later (p = 0.331) and social media use around bedtime (p = 0.298).  
* 76.9% of students (120/156) self-report being distracted by social media while actively doing schoolwork at least “sometimes”; 40.4% report it “often” or “all the time”; only 5.8% (9 students) report never being distracted by it.   
* Distraction correlates with procrastination ($\rho =0.491$), sleeping later ($\rho =0.467$), and average daily hours spent on social media ($\rho =0.347$), all q &lt; 0.0001.  
* Of the 23 students who reported not using social media, 11 (47.8%, 95% CI \[29, 67\]) said they feel like they are missing out on social connectedness as a result while 12 indicated they do not.

Students cited the following reasons for not using social media:

| Reason | n | % | 95% CI |
| :---- | :---- | :---- | :---- |
| Potential negative effects on mental health | 15 | 65.2% | \[44.9, 81.2\] |
| Lack of time or interest | 15 | 65.2% | \[44.9, 81.2\] |
| Parental restrictions | 12 | 52.2% | \[33.0, 70.8\] |
| Things seen can be fake or unrealistic | 9 | 39.1% | \[22.2, 59.2\] |
| Drama or negativity | 7 | 30.4% | \[15.6, 50.9\] |
| Data privacy / targeted advertisement concerns | 7 | 30.4% | \[15.6, 50.9\] |

An “other” option was included where participants were able to type in a free-text response as well. Some included cyberbullying, online grooming, and “brainrot.” 

## Summary of Findings

1. **Using social media within one hour of going to sleep and loss of sleep are significantly correlated** ($\rho =0.596$), and using social media around bedtime is incredibly common (72.4%).   
2. **Time spent per day on social media may predict certain habits but not feelings around social media.** Daily average time spent on social media is closely linked with use around bedtime and consciously putting off tasks (procrastination), but no correlations were found with any of the eight wellbeing items after correction.  
3. **Freshmen (9th graders) describe social media’s effect on themselves more negatively than seniors (12th graders)** on a single summary question ($p=0.0041$), even though both grades self-report very similar patterns of usage and behavior for all habits measured. Both indicate similar perceptions of social media’s impact on people their age. Interestingly, there is no trend after freshman year in self-reported effect of social media as student grade increases.  
4. **Female-identifying students report more of both negative and positive experiences on social media.** The largest gender gap was on social comparison (54% vs. 31%). However, gender does not predict time spent on social media, nor frequency of habits like lurking (viewing posts without interacting).  
5. **A student’s most-used social media platform does not predict the intensity of any of the habits tracked** once time spent is accounted for ($p=0.31$ unadjusted, $0.21$ adjusted).   
6. **Positive experiences outnumber negative ones** (3.27 vs. 1.56 on matched 0-8 scales) despite 72.4% of students indicating that they believe social media’s impact on people their age is “mostly negative.” There is a discrepancy of around 30 points between what students perceive about social media and what they actually report experiencing.  
7. **Students who post on social media report both more perceived benefits and (to some extent) drawbacks of social media use,** including showcasing creativity and being motivated to post for likes. They do not, however, report different effects in sleep quality/duration, distraction, or procrastination.

## Discussion

Students in this sample report substantially less social media use (a mean of around 2.08 hours per day) compared to the figure reported by the American Psychological Association in 2024 (a mean of around 4.8 hours per day for U.S. teens)[^1]. The median for our survey is about 1-2 hours, and only 10.9% (17 of 156\) self-reported 4+ hours of social media use per day. It is worth noting that this lower-than-average social media time per day may be due to a multitude of factors, including, but not limited to, the nature of the schools that were surveyed. Both are rigorous, highly competitive private schools in the Seattle/Greater Seattle Area, and one of the schools has a strict no-phone policy throughout campus during the school day. These factors should be taken into account when interpreting results; a population with comparatively lighter social media usage and different kinds of resources at its disposal may lead to different relationships observed compared to groups with heavier social media use on average. 

*We now establish a set of hypotheses we generated based on our prior research, and evaluate our data’s support or contradiction of each. We also provide disclaimers for each of these conclusions and any others drawn from the data under that topic.* 

**Hypothesis I:** Previous research has indicated that frequent social media use in the evening near bedtime is associated with a later sleep time, poorer sleep quality, and decreased duration of sleep. Since many social media apps have a built-in “infinite scroll” feature, adolescents may find it particularly challenging to refrain from lengthy scrolling at bedtime. Furthermore, exposure to the blue light emitted from device screens suppresses melatonin, a hormone that plays a key role in governing the sleep-wake cycle.

**Supported by our data.** The relationship between social media use in the evening near bedtime and later sleep time is the strongest out of the 66 pairwise correlations assessed in the survey. Note, however, that the association between using social media within one hour of going to bed and going to sleep later than planned still only had a correlation of 0.596. This means that the two measures share roughly 36% of their variance. This is a strong association for such a pairwise correlation; however, it still leaves a majority of variation in lost sleep unaccounted for. 

Furthermore, this type of correlational analysis does not establish directionality between the two variables, only correlation. Therefore, it is possible that users that are still awake late at night have greater opportunity to scroll instead of the late bedtimes being influenced by social media use. 

Overall, this correlation seems consistent with prior research on social media (and screens’) impact on sleep. With this in mind, it is a reasonable point of intervention or concern for social media users to bear in mind, even if direct causation cannot be established by the type of survey we conducted.

Finally, note that the impact of "infinite scroll” and blue light emitted from devices, along with quality of sleep, are not assessed in our survey. So, this part of the hypothesis remains untested and should be examined in the future for corroboration. 

**Hypothesis II:** Various correlational studies done in the past observed a positive relationship between time spent on social networks and academic procrastination. Many cited the displacement of focus time offline with heavy social media use as a way of avoiding or putting off school-related assignments.

**Supported by our data.** However, note the association is only moderate, with about 20% of variance shared between time spent and academic procrastination. This correlation is also potentially explained by the converse of the hypothesis; it is possible that students who are already procrastinating simply adopt social media as their distraction of choice over other actions, and social media may have no causation on procrastination if this is the case.   
Some free-responses from students indicated social media as a reason for procrastination: for example, one reported feeling “very guilty about being on YouTube shorts but can’t seem to stop.” However, this is only anecdotal and subjective, and cannot be used as an indicator of the actual directionality of the correlation factors. It was also not consistent across answers.

**Hypothesis III:** Various studies have suggested the idea of “developmental windows of sensitivity” during adolescence, wherein the negative effects of heavy social media use on academics and various aspects of social life are more pronounced in younger adolescents. 

**Somewhat supported by our data.** Specifically, the claim that freshmen differed from older students is more greatly supported, whereas the claim that vulnerability steadily declines with age or grade level is not statistically supported. Furthermore, since our survey is cross-sectional, it is difficult to judge what other mediating factors besides potential “developmental windows” of age might be affecting the results.

We cannot reliably determine what resulted in the gap between freshman responses and those of other grade-level students. One potential explanation is a difference in how self-critical students from different grades are of their own behavior, another might be the difference in high school experience/social adjustment across different years of schooling, and finally it might have something to do with neurological “developmental windows” as suggested by the hypothesis. Our survey did not have any means of distinguishing or weighting any of these factors. However, the survey found no evidence of a steady trend across all grade levels.

**Hypothesis IV:** Prior studies have outlined that female-identifying individuals have an increased likelihood of being adversely affected by time spent on social media, particularly when it comes to mental health (including symptoms of depression, body image problems, and disordered eating), whereas a direct correlation is seldom found in their male-identifying counterparts.

**Somewhat supported by our data.** First, note that the social comparison item was a proxy for the symptoms listed in this hypothesis – we did not rigorously test each symptom on its own. Additionally, the effects lean towards self-reported experiences on social media rather than time spent; the data found that gender is not significantly associated with time spent at all $(p=0.257$). Crucially, the pattern is also not one-directional; female students reported more positive experiences as well as negative ones. Furthermore, effect sizes are small to moderate throughout self-reported mental health factors (r\_rb  ≈ 0.21–0.34) in general.

Other gender identities unfortunately did not have sufficient sample size in this survey to make large-scale conclusions.

*Next, we summarize the most important additional trends based purely on personally-perceived effects.* These results should be inherently interpreted with some skepticism given the potential increase in biases that arises with direct self-reporting. 

Of the 66 pairwise correlations, only 3 being largely significant ($\left|{\rho }\right|\geq 0.50$) and 17 being moderate (0.30-0.50) may suggest that the relationships between self-report factors vary a lot student-by-student. This is further supported by habit-clustering in the data; students reporting one habit related to social media use also tended to report other habits, indicating that some students are potentially heavily impacted (whether positively, negatively, or neutrally) while others are not at all impacted. 

At the same time, the association between daily average social media use and students’ rating of social media’s effect was weak and tenuous. One explanation for this is that some students who use social media more might be more connected to a greater number of people through it, or get recommended more engaging content, which could provide benefits in addition to any possible drawbacks and change their self-report rating. Another is that there are not sufficient drawbacks (whether objectively or ones that people notice) for people to report social media as having negative effects at all. The third possibility, suggested by some written responses, is that certain people believe there are significant negative effects, and other people believe there are no effects at all, and this range of opinions on the individual level results in scattered data. Further investigation might be needed to determine the exact reason for this result, but it is interesting in that it perhaps contradicts a common opinion that people who use social media a lot are not overall satisfied with the effects it has on their lives. 

93.9% of the respondents that did rate social media as having a “mostly negative” impact cited concern about time spent. However, time spent does not seem to have a strong relationship with the actual perceived effect of social media that respondents collectively reported. This potentially implies that respondents are worried about time even if their actual hours spent on social media do not consistently predict their well-being or feeling.

Respondents reported positive experiences more often than negative ones. However, while the overall experience is net-positive, this does not indicate that social media is strictly a positive or negative force in students’ lives. 43.6% of respondents reported feeling worse about their lives compared to others when using social media, and around a third reported feeling left out by friends. Rates like this are still significant to note as a well-being measure, and show that social media can have both positive and negative impacts. 

The individual habit that was most associated with negative feeling is displacement of in-person time by social media. The effect of this was moderate-to-high ($\rho =0.379$ correlation coefficient between displacement of in-person time and negative-feelings-score), but it is important to consider that it was also the least commonly reported habit with only 8.3% (13/156, 95% CI \[4.9, 13.7\]) reporting doing it “often” or “all the time.”). So, it may not have significant bearing on the “typical” social media user.

The choice of primary platform that respondents used accounted for around 3% of differences in habit scores, although this could be explained by the mediator of total time spent on social media rather than platform type as well. In general, for results involving platform type it is impossible to rank platforms with 3-6 primary users meaningfully. Just one respondent can move the results immensely due to the small sample size (see [*Sample size (a.) Small & uneven sample sizes across platforms*](#2a-small-uneven-sample-sizes-across-platforms) in [Limitations](#limitations) section for more information). So, the data does not support any particular conclusions about platform type; instead, it supports general takeaways about time-related habits spent across all platforms. 

Users who posted reported both more benefits and more costs on average, with no statistically significant differences in sleep, procrastination, or distraction. One hypothesis explaining this is that posters are more engaged users, and therefore inherently experience more intense positive and negative experiences during their use. The relationship may also be directed in the reverse order, in part or in full; people who feel more connected may post more and that could produce these results. Finally, a secondary hypothesis stems from the fact that students reported posting largely their accomplishments on social media: perhaps posting accomplishments is especially conducive to either feeling good about oneself or feeling left out, while the other factors are not related to it in comparison to other kinds of posts. 

Finally, an overall interpretation from the pairwise associations we established is that factors like sleeping later due to social media use, comparing one’s self to others on social media, and letting social media displace in-person interactions are more closely tied to social media’s negative impacts on students than time spent on social media alone. Specifically, once lost sleep is accounted for, the association between total daily hours spent on social media and perceived effect on one’s self substantially weakens. 

*Last, we discuss non-significance results.*

It is possible that many of the non-significant results we report simply did not have enough certainty. So, these relationships might still exist if we looked at a greater sample size of adolescents – they would just present themselves as a weak correlation among the data, which we had to discard in the context of this survey due to sample size. See [*Sample Size*](#2-sample-size) in [Limitations](#limitations) section for more information.

## Limitations

### 1. Sampling and generalizability

One of the schools surveyed had a phone ban in place at the time of the survey, while the other did not. Since we did not distinguish between response pools across the two schools for privacy reasons, this may have introduced some variance across response groups into the collective data. 

Furthermore, both schools surveyed are highly selective, rigorous private schools in the Greater Seattle Area, and have small student bodies relative to most public schools. This may limit applicability of results to a broader adolescent, high-school-student population.

There may have also been volunteer bias in the survey results. Namely, since the survey was entirely voluntary for students across both schools, it is possible that people with relatively stronger opinions on social media would respond to a survey about social media, and others would not (for example; or, alternatively, people spending a great amount of time on social media might not have the time/desire to respond to a survey).

### 2. Sample size

With a sample size of N = 156 students, the survey can only reliably detect correlations greater than around $\left|{\rho }\right|=0.22$. We categorized some trends near this value as significant but extremely weak, but values which were much lower than this in significance we categorized as broadly “not significant at all.” This may or may not accurately reflect the true relationship between factors; it is possible that with a larger sample size there would be a weak-but-present correlation established between some of those factors. 

<div class="li_subsection" markdown>
#### 2a. Small & uneven sample sizes across platforms

For conclusions about differences between platforms, the sample sizes were very inconsistent as there was a large spread of total platforms, but Instagram and YouTube had by far the greatest user base among survey respondents. So, the small sample sizes of other platforms introduce more uncertainty into results about platform-specific effects. 
</div>

### 3. Self-reported & subjective data

Since data was self-reported, there may be social desirability bias (the desire to present oneself as having more societally-accepted habits or values than one’s actual values) in responses. Similarly, there might be bias or inaccurate recollection in people’s memory of their own use. We attempted to counteract this by directing people to check their devices’ built-in screentime trackers for quantitative metrics like time spent on social media; however, it is possible survey respondents did not follow this to save time. It is also possible that screentime trackers varied in how they measured screen time or time-per-app, leading to inaccuracy in comparison. Finally, there was no way to counteract inaccurate recollection for qualitative, experience-based questions.

<div class="li_subsection" markdown>
#### 3a. Third-person effect

The third-person effect states that people are more likely to believe mass media/society’s messaging impacts others negatively compared to themselves[^2]. This effect may have biased respondents to claiming social media has negative effects for peers as a whole, but reporting less negative effects for themselves in the survey.
</div>

### 4. Correlation doesn’t equal causation & confounding factors

Due to the cross-sectional nature of the survey questions, there is no way to establish causal direction between factors. We could not control for other factors, such as school pressure, family situation, financial situation, and more–all of which can influence social media usage habits, adolescent well-being, and metrics we measured like sleep time. 

We can also not definitively say whether people spending time on social media is causing any self-reported effects or habits, or whether people that already have those self-reported habits or experience those effects from other activities are simply more likely to use social media extensively.

Overall, although the associations are consistent with a directional relationship and we can form stronger hypotheses around them, this survey design cannot rigorously test for such a relationship.

## Conclusion & Future Directions

Our survey generally found that the ways high school adolescents used social media – for example, use near bedtime, social comparison tendencies and displacement of in-person time – mattered more for differences in well-being factors and use experience than the total amount of hours spent. The most significant findings are the association between bedtime social media use and going to sleep later than planned, the gap in perception of social media’s negative impact on other peers than respondents themselves, and more negative self-rated effect in freshmen compared to other grades. 

Broadly speaking, experiences with social media were positive for students, although meaningful minorities reported struggling with comparison online, feeling a sense of exclusion from friends, and losing sleep. We therefore hypothesize that social media is not negatively impacting most students in a significant way and, for those students, is actually a positive force. However, some students might experience it more negatively than others, and using healthy intervention strategies becomes important for those individuals to improve their well-being. 

Bearing in mind that this survey was cross-sectional, self-reported, and limited to two private high schools, future directions of this survey should involve longitudinal experiments. This addresses the limitation of not having a causal direction between factors like age and social media experience; by tracking the same students over time, we could see how age might change social media use and effects without worrying about individual-based confounding factors. Similarly, we could introduce a robust experimental design to change one independent factor and observe social media use experience (for example, testing a bedtime-use reduction for a large population of students). 

Furthermore, future iterations should have larger samples to address generalizability; if possible, we want to extend this to public schools and have enough respondents to encompass many gender identities. Another interesting direction is to factor in socioeconomic status/class, although this may run into user data concerns. Finally, to maximize quantitative accuracy, implementing a standardized app to log usage across many kinds of devices would be an improvement over the current self-report process.   

Another possible direction for future work is conducting more qualitative interviews in place of the written responses. We could then categorize those responses more rigorously into buckets to expand upon the details of individual usage experience. 

[^1]: [Teens are spending nearly 5 hours daily on social media. Here are the mental health outcomes](https://www.apa.org/monitor/2024/04/teen-social-use-mental-health)
[^2]: [The Third Person Effect in Communication](https://doi.org/10.1086/268763)