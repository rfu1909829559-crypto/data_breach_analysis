# Data Breach Analysis Report

## 1. Introduction
The analysis of global data breaches is driven by the need to provide practical insights for governments and industries seeking to strengthen their domestic data protection strategies. By examining both the frequency of breach incidents and the scale of records lost, this study aims to highlight patterns that can inform more efficient allocation of time, resources, and capital in cybersecurity.

### Scope
The scope of the research covers two complementary dimensions: the number of incidents and the total volume of records lost. These indicators are analyzed across temporal trends, country-level distributions, and sectoral distributions. Comparing incident counts with data loss volumes allows for a clearer understanding of whether risks are concentrated in frequent small breaches or in fewer but larger-scale events.
### Objective
The objectives are threefold: first, to identify long-term temporal trends in data breaches; second, to determine which countries and sectors are most frequently affected; and third, to raise new questions that emerge from preliminary tabulations, such as discrepancies between incident frequency and data volume.

While the contribution of this study is still being refined, its importance lies in the fact that the internet has only existed for a few decades. At this early stage of digital history, identifying emerging patterns in data breaches is crucial for understanding the evolving landscape of cybersecurity risks and for guiding proactive responses in policy and industry practice.


## 2. Data and Methods

### 2.1 Data Source
The dataset used in this study is derived from the Kaggle public dataset **“World’s Biggest Data Breaches & Hacks (2004–2025)”**  
(https://www.kaggle.com/datasets/awallay/worlds-biggest-data-breaches-and-hacks-2004-2025).  
The cleaned version (`worlds_biggest_breaches_cleaned.csv`) was downloaded and used as the primary input.  
Additionally, a manually curated file (`Naming.csv`) was created to map each organisation to its corresponding ISO3 country code.  
This mapping was necessary because the original Kaggle dataset did not include standardized country identifiers.

### 2.2 Data Structure
The cleaned dataset contains the following fields:

- **organisation** – name of the affected company or institution  
- **alternative name** – secondary or short name  
- **records_lost** – number of records compromised  
- **year** – year of the breach  
- **date** – exact date of the breach (when available)  
- **story** – description of the incident  
- **sector** – industry classification (e.g., web, government, health, retail)  
- **method** – attack method (e.g., hacked, poor security, inside job)  
- **interesting story** – flag for notable incidents  
- **data sensitivity** – qualitative measure of sensitivity (scale 1–4)  
- **displayed records** – formatted version of records lost (e.g., “2.7bn”)  
- **source name** – reporting source  
- **1st source link / 2nd source link** – references to original articles  
- **ID** – unique identifier for each incident  
- **iso3** – manually added ISO3 country code (from `Naming.csv`)

### 2.3 Preprocessing Workflow
Since the dataset was already cleaned, preprocessing was minimal but essential:
1. **Merge** – combined `worlds_biggest_breaches_cleaned.csv` with `Naming.csv` to add ISO3 codes.  
2. **Encoding Fix** – manually corrected UTF-8/Latin1 parsing errors that prevented automatic merging.  
3. **Finalize Dataset** – ensured all organisations had valid ISO3 codes and consistent sector labels.  

This workflow guarantees reproducibility and ensures that country-level analysis is possible.

### 2.4 Analytical Methods
The analysis was conducted through descriptive statistics and visualization.  
Key steps included:

- **Annual Trends** – grouped by `year` to calculate total records lost and incident counts; plotted as line graphs.  
- **Country Distribution** – aggregated by `iso3` to compare records lost and incident counts across countries; visualized with bar charts and a world map.  
- **Sector Distribution** – grouped by `sector` to compare records lost and incident counts across industries; visualized with bar charts.  
- **Heatmap Analysis** – created a pivot table (`year × sector`) to show records lost; plotted as a heatmap.  
- **Proportional Analysis** – calculated sectoral shares of records lost and incident counts per year; plotted as multi-line charts.  

These methods allow direct comparison between **incident frequency** and **data volume**, highlighting differences in risk concentration.

### 2.5 Tools and Environment
All analysis was performed in the following environment:

- **Python 3.14 (64-bit)**  
- **Libraries**: pandas, matplotlib, seaborn  
- **IDE/Notebook**: Jupyter Notebook / PyCharm  
- **Operating System**: Windows 11 (64-bit)  

This setup ensures reproducibility and compatibility with standard data science workflows.


## 3. Results

### 3.1 Annual Trends
- **Figure 1: Total Records Lost per Year**
- **Figure 2: Number of Breaches per Year**
### Total Records Lost per Year & Number of Breaches per Year

The annual trends reveal two distinct perspectives on data breaches.  
In **Total Records Lost per Year**, the volume of compromised records remained relatively flat until around 2012, after which it began to fluctuate sharply. Between 2014 and 2018, the overall trajectory was upward, culminating in a peak in 2018. Following this peak, the trend declined but continued to exhibit large oscillations, making it difficult to define a stable long-term pattern.  

In contrast, **Number of Breaches per Year** shows a clearer upward trajectory. Although the number of incidents fluctuates, the overall direction is one of steady increase, with notable peaks around 2012, 2018, and 2023.  

A comparative view highlights important discrepancies. Years such as **2008, 2011, 2020, 2023, and 2025** recorded relatively high incident counts but comparatively low volumes of records lost, suggesting that these periods were dominated by numerous smaller-scale breaches. Conversely, years such as **2016–2018, 2021, 2022, and 2024** saw fewer incidents but disproportionately large data losses, indicating the presence of a small number of extremely large breaches.  

This divergence underscores the importance of analyzing both frequency and scale. Incident counts alone may exaggerate the perception of risk if the breaches are minor, while record volumes alone may obscure the prevalence of smaller but frequent attacks. Together, these measures reveal that the dynamics of data breaches are shaped by both the number of events and the magnitude of individual incidents.

### 3.2 Country/Region Analysis
### Total Records Lost per Country/Region & Number of Breach Incidents per Country/Region
- **Figure 3: Total Records Lost per Country/Region**
- **Figure 4: Number of Breaches per Country/Region**
The country-level comparison reveals a striking imbalance.  
In **Total Records Lost per Country/Region**, the United States stands out as an extreme outlier, with data loss volumes far exceeding all other countries. By contrast, most other nations cluster at significantly lower levels, with Indonesia, India, and China following distantly behind.  

In **Number of Breach Incidents per Country/Region**, the United States again leads by a wide margin, recording more than 300 incidents. The next tier of countries—United Kingdom, Japan, and Germany—show considerably fewer incidents, yet still occupy the second, third, and fourth positions in frequency.  

A comparative view highlights important differences. While the United States dominates both dimensions, Indonesia, India, and China rank highly in total records lost but much lower in incident counts (18th, 8th, and 9th respectively). This suggests that these countries experienced fewer breaches overall, but those breaches were exceptionally large in scale. Conversely, the United Kingdom, Japan, and Germany rank near the top in incident counts but not in total records lost, reflecting a pattern of numerous smaller breaches rather than a few massive ones.  

Indonesia represents a particularly notable case: despite ranking second in total records lost, it is only 18th in incident counts. This discrepancy suggests a small number of extremely large breaches, and warrants further investigation in the **Future Research** section to understand the structural or contextual factors behind this anomaly.  

These discrepancies point to structural differences in how breaches manifest across countries. Large-scale losses in India and China may be linked to population size and the presence of centralized national databases, where a single breach can expose vast amounts of data. Legal and industry practices may also play a role, as disclosure requirements differ across jurisdictions. In contrast, countries such as the UK and Japan, with strong corporate disclosure norms and many domestic enterprises, tend to report frequent but smaller-scale incidents. Germany occupies an intermediate position, reflecting its role as both a national hub and part of the broader EU enterprise ecosystem.  

Together, these findings underscore the need to analyze both frequency and scale at the national level. The United States remains an extreme outlier in both measures, raising the central research question of why its breach volume and incident count are so disproportionately high compared to the rest of the world.


### 3.3 Sectoral Analysis
- **Figure 5: Total Records Lost per Sector**
- **Figure 6: Number of Breaches per Sector**

The sector-level comparison highlights the dominance of the **web** and **government** industries.  
In **Total Records Lost per Sector**, the web sector is by far the largest contributor, with data loss volumes significantly higher than all other industries. Government and telecoms follow at a distant second and third, while the remaining sectors show progressively smaller values.  

In **Number of Breaches per Sector**, the web sector again leads, recording more than 140 incidents. Government, health, retail, and finance occupy the next positions, each with around 50 incidents, while other sectors trail behind with much lower counts.  

A comparative view shows that the web and government sectors are consistently at the top in both dimensions, reflecting both frequent attacks and large-scale losses. However, differences emerge in other industries. For example, the health sector ranks high in incident counts but not in total records lost, suggesting frequent smaller breaches. Conversely, telecoms rank high in total records lost but not in incident counts, indicating fewer but more severe breaches.  

These discrepancies can be explained by structural characteristics of the industries. The web sector is dominated by global platforms with vast user bases, making them attractive targets for attackers and ensuring that both the frequency and scale of breaches are high. Many of these companies are headquartered in the United States, which helps explain why the U.S. consistently ranks as the global leader in both breach counts and data loss volumes. Government databases, by contrast, are highly integrated at the national level, so breaches tend to expose large amounts of citizen data even if the number of incidents is relatively limited.  

Together, these findings underscore the importance of distinguishing between **frequency-driven risk** (e.g., health, retail) and **scale-driven risk** (e.g., telecoms, government). The web sector remains unique in combining both dimensions at extreme levels, making it the single most significant driver of global data breach statistics.


### 3.4 Heatmap of Records Lost by Year and Sector
- **Figure 8: Heatmap of Records Lost by Year and Sector**

The heatmap provides a combined view of temporal and sectoral dynamics in data breaches.  
It shows that the most significant losses are concentrated in the **web** and **tech** sectors, particularly during the years **2018–2020**, when multiple large-scale incidents occurred. These sectors display darker shades across several consecutive years, indicating sustained vulnerability rather than isolated events.  

Other industries such as **government** and **health** also show notable losses, but their peaks are more sporadic and tied to specific years rather than continuous exposure. For example, government-related breaches appear in distinct bursts, reflecting the episodic nature of attacks on centralized national databases. Health sector losses, while smaller in scale compared to web and tech, are distributed across multiple years, suggesting recurring exposure of sensitive patient data.  

The visualization highlights two important patterns. First, the **web and tech sectors dominate both in frequency and scale**, reinforcing earlier findings that global platforms are the most attractive targets for attackers. Second, the **temporal clustering of severe breaches** around 2018–2020 suggests that certain periods may be associated with heightened vulnerability, possibly due to technological transitions, regulatory gaps, or the emergence of new attack methods.  

This combined perspective underscores the need to analyze breaches not only by sector but also by their timing. It raises further questions about whether specific global events or technological shifts contributed to the surge in losses during 2018–2020, and whether similar clustering might recur in future years.

### 3.5 Sector Share of Records Lost Over Time & Sector Share of Incident Count Over Time

The longitudinal comparison of sectoral shares provides insight into how the relative importance of different industries has shifted over time.  
In **Sector Share of Records Lost Over Time**, the early years show occasional dominance by sectors such as web and finance, likely reflecting the limited number of recorded incidents and the absence of systematic reporting. During the 2010s, however, the **web sector emerges as the clear leader**, consistently accounting for the largest share of records lost. This dominance begins to diminish in the early 2020s, when the distribution of shares becomes more balanced across multiple sectors. This shift may indicate either a change in attacker focus away from web platforms or improvements in data collection and reporting that highlight breaches in other industries.  

In **Sector Share of Incident Count Over Time**, the web sector again dominates throughout the 2010s, reflecting both its global exposure and the frequency of attacks. However, the early 2020s show a more diversified pattern, with government, health, and retail sectors gaining relative prominence. This suggests that while web platforms remain critical targets, other industries have become increasingly visible in breach statistics.  

A comparative view highlights the divergence between **frequency and scale**. Web platforms dominate both dimensions during the 2010s, but by the 2020s their relative share of records lost declines even as incident counts remain high. Health and retail sectors, by contrast, show rising shares in incident counts but not in records lost, reflecting frequent smaller breaches. Telecoms and government sectors exhibit the opposite pattern: fewer incidents but disproportionately large data losses.  

These findings reinforce earlier conclusions about the distinction between **frequency-driven risk** and **scale-driven risk**, while also raising new questions. The clustering of web dominance in the 2010s followed by a more balanced distribution in the 2020s suggests a structural shift in the breach landscape. Future research should explore whether this reflects changes in attacker strategies, improvements in web security, or simply more comprehensive reporting across diverse industries.


## 4. Discussion
### Discussion

The analysis reveals several overarching patterns in the global data breach landscape.  
Most prominently, the **United States and the web sector emerge as dominant outliers**, consistently leading both in incident frequency and in total records lost. This dual dominance underscores the structural role of U.S.-based global platforms in shaping breach statistics. At the same time, the data suggest that the **web sector’s dominance may be weakening in the early 2020s**, as shares of both records lost and incident counts become more evenly distributed across industries. This shift points to a possible transition in attacker strategies or improvements in web security, and should be monitored closely in future research.  

Several mechanisms help explain these patterns. The **location of corporate headquarters** plays a critical role, with many of the largest web companies based in the United States, thereby concentrating both exposure and reporting. **Population size** also matters: breaches in countries such as India and China often involve centralized national databases, where a single incident can compromise vast amounts of citizen data. **Legal disclosure regimes** further shape the dataset, as countries with stronger transparency requirements (e.g., the U.S., UK, Japan) report more incidents, while countries with weaker disclosure norms may underreport, leading to apparent disparities.  

The temporal dimension adds another layer of complexity. The **2018–2020 period stands out as a cluster of extreme losses**, particularly in the web and tech sectors. Several factors likely contributed to this surge. First, the rise of **ransomware and “double extortion” attacks** during this period meant that attackers not only encrypted data but also leaked it when victims refused to pay, dramatically increasing the volume of exposed records. Second, the implementation of **new regulatory frameworks such as the EU’s GDPR in 2018** led to a sharp increase in the number of publicly disclosed breaches, amplifying the apparent scale of incidents. Third, **technological transitions**—including rapid adoption of cloud services and API-driven architectures—created new vulnerabilities that attackers exploited. Finally, **geopolitical tensions and the activity of state-linked groups** further intensified the scale and visibility of breaches.  

In contrast, the early 2020s show a more balanced distribution across sectors, suggesting either diversification of attacker focus or improved data collection practices. This shift may indicate that the breach landscape is evolving, with web platforms no longer the sole dominant targets and other industries increasingly exposed.
  

This study is not without limitations. The dataset relies on **publicly disclosed breaches**, and transparency varies widely across countries and industries. Nations with strong disclosure requirements may appear disproportionately vulnerable, while those with weaker regimes may underreport, obscuring the true scale of breaches. Additionally, the dataset may miss incidents that were never publicly acknowledged, introducing potential bias.  

Despite these limitations, the findings carry important implications. Policymakers and industry leaders should recognize the **continued vulnerability of internet-based enterprises**, while also preparing for a possible shift in breach dynamics as other sectors gain prominence. The distinction between **frequency-driven risk** (many small breaches) and **scale-driven risk** (few but massive breaches) is critical for resource allocation and regulatory design. Finally, the observed changes in sectoral dominance highlight the need for vigilance against **inertia in risk perception**: the breach landscape is evolving, and strategies must adapt accordingly.


## 5. Conclusion

This study provides a comprehensive analysis of global data breaches across temporal, geographic, and sectoral dimensions. The findings highlight several consistent patterns. Most notably, the **United States and the web sector dominate both in incident frequency and in total records lost**, underscoring their outsized role in shaping the breach landscape. At the same time, the data reveal important divergences between **frequency-driven risk** (many small breaches, as seen in health and retail) and **scale-driven risk** (few but massive breaches, as seen in telecoms and government).  

The temporal analysis identifies the **2018–2020 period as a turning point**, marked by concentrated large-scale losses in web and tech sectors, followed by a more balanced distribution in the early 2020s. This suggests that the breach landscape is dynamic, with sectoral dominance shifting over time. Geographic comparisons further emphasize structural differences: countries with large populations and centralized databases (e.g., India, China, Indonesia) tend to experience fewer but larger breaches, while nations with strong disclosure regimes (e.g., the U.S., UK, Japan) report more frequent but smaller incidents.  

Together, these results underscore the importance of analyzing breaches through multiple lenses—frequency, scale, geography, and sector. They also caution against inertia in risk perception: while web platforms remain critical targets, the evolving distribution of breaches across industries and regions suggests that future vulnerabilities may emerge in new and unexpected domains.

## 6. Future Research

Several avenues for future research emerge from this study.  
First, the **2018–2020 surge in data losses** warrants closer investigation. This period coincided with the rise of ransomware “double extortion” attacks, the implementation of GDPR and other disclosure regimes, and rapid technological transitions such as cloud migration. Future work should examine how these factors interacted to produce concentrated large-scale breaches, and whether similar clustering may recur under comparable conditions.  

Second, the case of **Indonesia** represents a notable anomaly. Despite ranking second in total records lost, it is only 18th in incident counts. This suggests a small number of exceptionally large breaches, raising questions about the structural or contextual drivers of such disproportionate outcomes. Future studies could explore whether specific national databases, industry practices, or disclosure norms explain this divergence.  

Third, the **web sector’s dominance appears to be weakening in the early 2020s**, with breach shares becoming more evenly distributed across industries. This shift may reflect changes in attacker strategies, improvements in web security, or more comprehensive reporting in other sectors. Future research should track whether this trend continues, and what it implies for the evolving distribution of risk across industries.  

Finally, the broader distinction between **frequency-driven risk** and **scale-driven risk** deserves systematic exploration. Understanding why some sectors experience many small breaches while others suffer few but massive incidents could inform both regulatory design and resource allocation. Comparative studies across countries and industries would help clarify how population size, corporate headquarters location, and disclosure regimes shape these divergent risk profiles.


## 7. Appendix

- **CSV outputs**  
  All processed datasets used in this study are available in structured CSV format (e.g., `process_data/country_sector_incidents.csv`). These files contain the cleaned and aggregated data underlying the figures presented in the Results section.  

- **Code snippets for reproducibility**  
  Selected Python scripts and code snippets are included to ensure reproducibility of the analysis. These cover data preprocessing, visualization generation, and statistical summaries. The repository provides clear documentation for replicating the workflow and verifying results.  

- **Supplementary figures and tables**  

  Additional charts and tables not included in the main text are provided to illustrate intermediate steps, robustness checks, and alternative visualizations.  

- **Methodological notes**  
  Detailed notes on data sources, inclusion/exclusion criteria, and handling of controversial or incomplete cases are documented to support transparency and methodological rigor.