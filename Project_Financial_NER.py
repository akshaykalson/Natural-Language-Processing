#here we are creating a project to analyse news articles for stocks that are in our portfolio
# so that we can get news related to our stocks

import spacy
import pandas as pd

df = pd.read_csv('resources/stocks.csv')

symbols = df.Symbol.tolist()
companies = df.SecurityName.tolist()
print(symbols[:10])
print(companies[:20])
patterns = []
nlp = spacy.blank('en')
ruler = nlp.add_pipe('entity_ruler')
for symbol in symbols:
    patterns.append({"label": "STOCK", "pattern": symbol})

for company in companies:
    patterns.append({"label": "COMPANY", "pattern": company})
ruler.add_patterns(patterns)

#source: https://www.reuters.com/business/futures-rise-after-biden-xi-call-oil-bounce-2021-09-10/
text = '''
Sept 10 (Reuters) - Wall Street's main indexes were subdued on Friday as signs of higher inflation and a drop in Apple shares following an unfavorable court ruling offset expectations of an easing in U.S.-China tensions.

Data earlier in the day showed U.S. producer prices rose solidly in August, leading to the biggest annual gain in nearly 11 years and indicating that high inflation was likely to persist as the pandemic pressures supply chains. read more .

"Today's data on wholesale prices should be eye-opening for the Federal Reserve, as inflation pressures still don't appear to be easing and will likely continue to be felt by the consumer in the coming months," said Charlie Ripley, senior investment strategist for Allianz Investment Management.

Apple Inc (AAPL.O) fell 2.7% following a U.S. court ruling in "Fortnite" creator Epic Games' antitrust lawsuit that stroke down some of the iPhone maker's restrictions on how developers can collect payments in apps.


Sponsored by Advertising Partner
Sponsored Video
Watch to learn more
Report ad
Apple shares were set for their worst single-day fall since May this year, weighing on the Nasdaq (.IXIC) and the S&P 500 technology sub-index (.SPLRCT), which fell 0.1%.

Sentiment also took a hit from Cleveland Federal Reserve Bank President Loretta Mester's comments that she would still like the central bank to begin tapering asset purchases this year despite the weak August jobs report. read more

Investors have paid keen attention to the labor market and data hinting towards higher inflation recently for hints on a timeline for the Federal Reserve to begin tapering its massive bond-buying program.

The S&P 500 has risen around 19% so far this year on support from dovish central bank policies and re-opening optimism, but concerns over rising coronavirus infections and accelerating inflation have lately stalled its advance.


Report ad
The three main U.S. indexes got some support on Friday from news of a phone call between U.S. President Joe Biden and Chinese leader Xi Jinping that was taken as a positive sign which could bring a thaw in ties between the world's two most important trading partners.

At 1:01 p.m. ET, the Dow Jones Industrial Average (.DJI) was up 12.24 points, or 0.04%, at 34,891.62, the S&P 500 (.SPX) was up 2.83 points, or 0.06%, at 4,496.11, and the Nasdaq Composite (.IXIC) was up 12.85 points, or 0.08%, at 15,261.11.

Six of the eleven S&P 500 sub-indexes gained, with energy (.SPNY), materials (.SPLRCM) and consumer discretionary stocks (.SPLRCD) rising the most.

U.S.-listed Chinese e-commerce companies Alibaba and JD.com , music streaming company Tencent Music (TME.N) and electric car maker Nio Inc (NIO.N) all gained between 0.7% and 1.4%


Report ad
Grocer Kroger Co (KR.N) dropped 7.1% after it said global supply chain disruptions, freight costs, discounts and wastage would hit its profit margins.

Advancing issues outnumbered decliners by a 1.12-to-1 ratio on the NYSE and by a 1.02-to-1 ratio on the Nasdaq.

The S&P index recorded 14 new 52-week highs and three new lows, while the Nasdaq recorded 49 new highs and 38 new lows.
Home  >  News & Events  >  News  >  News Details
News Details
OverviewWhy AgilentNews & EventsStock InfoFinancialsGovernanceShareholder Resources
Investors Search
Agilent Announces Cutting-Edge Advances in GC/MS and LC/Q-TOF Technology at ASMS 2024
June 3, 2024
SANTA CLARA, Calif.--(BUSINESS WIRE)-- Agilent Technologies Inc., (NYSE: A) is introducing two new products at the 72nd ASMS Conference on Mass Spectrometry and Allied Topics. The Agilent 7010D Triple Quadrupole GC/MS System which targets the food and environmental markets, offers precision and sensitivity in gas chromatography-mass spectrometry. Additionally, the Agilent ExD Cell for use with the 6545XT AdvanceBio LC/Q-TOF system, serves the biopharma market and life science research. These instruments exemplify Agilent’s unwavering commitment to advancing scientific discovery through innovative instrumentation, significantly shaping the landscape of mass spectrometry.

The Agilent 7010D Triple Quadrupole GC/MS System (7010D GC/TQ) features the new HES 2.0 ion source, providing attogram-level sensitivity, unmatched robustness, and industry-leading uptime. Built-in intelligence, including SWARM autotune and Early Maintenance Feedback (EMF), streamlines analytical workflows and reduces unplanned instrument downtime, making it a reliable partner in navigating evolving regulatory requirements.

The 7010D GC/TQ also includes the My Green Lab Accountability, Consistency, and Transparency (ACT) Label, reflecting environmentally conscious manufacturing practices. Additionally, the MassHunter Acquisition 13.0 software enhances user experience with a refreshed interface and compliance tools, enabling users to take control of data integrity and adhere to compliance guidelines such as FDA 21 CFR Part 11, EU Annex 11, and GAMP5.

The Agilent ExD Cell available for the 6545XT AdvanceBio LC/Q-TOF enhances peptide and protein characterization capabilities by adding electron capture dissociation (ECD). With the trend towards increasingly complex biotherapeutics this meets the need for more thorough structural characterization.

The field installable ExD cell addon for the 6545XT is designed for researchers in the ‘discovery phase’ who are faced with diverse analytical challenges. ECD is particularly appropriate for the study of large proteins, fragile modifications, and isomeric residues – analytes which can be difficult to unambiguously characterize with traditional collision induced dissociation (CID) methods alone.

Coupled with the inherent capabilities of the 6545XT for intact protein analyses, the ExD cell is also suited for performing top to middle down characterization of large and highly charged proteins (such as antibodies) and smaller subunits (such as peptides), and the rich spectra produced can be interpreted with confidence using the ExDViewer.

“Intelligence capabilities are seamlessly integrated into instruments like the 7010D GC/TQ, recognizing the fiercely competitive landscape that is constantly evolving. Additionally, the Agilent ExD cell, in conjunction with the 6545XT AdvanceBio LC/Q-TOF, empowers scientists to meticulously scrutinize and more effectively characterize peptides—critical components in modern research and therapeutics,” stated Ken Suzuki, vice president and general manager of Agilent’s Mass Spectrometry Division.

“These cutting-edge products exemplify customer-driven innovation and excellence. By listening to our customers, we gain valuable insights into their challenges. We then channel this understanding into consistent innovation, resulting in outstanding products that precisely meet their needs,” added Suzuki.

Agilent is a leading solution provider of proven, robust, and reliable mass spectrometry technologies to a range of segments and a wide array of applications in the bio/pharma, life science research, food, and environmental markets. These new technological capabilities enable Agilent’s customers to increase data quality and interpretation while reducing the time and human attention required—more easily adapting to ever-changing market needs.

About Agilent Technologies

Agilent Technologies Inc. (NYSE: A) is a global leader in analytical and clinical laboratory technologies, delivering insights and innovation that help our customers bring great science to life. Agilent’s full range of solutions includes instruments, software, services, and expertise that provide trusted answers to our customers' most challenging questions. The company generated revenue of $6.83 billion in fiscal 2023 and employs approximately 18,000 people worldwide. Information about Agilent is available at www.agilent.com . To receive the latest Agilent news, please subscribe to the Agilent Newsroom. Follow Agilent on LinkedIn and Facebook.



Naomi Goumillout

Agilent Technologies, Inc.
'''
doc = nlp(text)
for ent in doc.ents:
    print(ent.text, ent.label_)

