class PromptTemplate:
    TOPIC_TO_ABSTRACST = '''
    Write an abstract of a scientific paper based on these topics and keywords.
    \n\n\n
    ###
    \n\n\n
    topics: \n
    Recommender systems\n
    Filtering\n
    Electronic commerce\n
    abstract: With the collaborative filtering techniques becoming more and more mature, recommender systems are widely used nowadays, especially in electronic commerce and social networks. However, the utilization of recommender systems in academic research itself has not received enough attention. A research paper recommender system would greatly help researchers to find the most desirable papers in their fields of endeavour. Due to the textual nature of papers, content information could be integrated into existed recommendation methods. In this paper, we proposed that by using topic model techniques to make topic analysis on research papers, we could introduce a thematic similarity measurement into a modified version of the item-based recommendation approach. This novel recommendation method could considerably alleviate the cold start problem in research paper recommendations. Our experiment result shows that our approach could recommend highly relevant research papers.
    \n\n\n
    ###
    \n\n\n
    topics: \n
    Corona\n
    Loss measurement\n
    Rain\n
    abstract: Transmission line corona loss research is one of the critical technologies of 1000 kV UHV transmission and transformation engineering. Transmission line corona loss relates to many factors of climate, and rainfall rate affects corona loss distinctly very much. By means of UHV AC single circuit test line, corona loss monitoring and UHV corona cage conductor corona loss measurement, this paper researched the effect of rainfall rates on UHV AC single-circuit transmission line's corona loss. This paper applied a corona loss monitoring system to monitor corona loss of UHV single circuit test line and obtained corona loss monitoring data in light rain, moderate rain, and heavy rain conditions. Analyze corona loss test results. Corona loss values in light rain, moderate rain, and heavy rain conditions are obtained. The results show that rain has an obvious influence on corona loss of the line, at the beginning of rain, corona loss increases quickly, after rain, corona loss decreases with the drying of the conductor. The decay time is related to surface field strength, wind speed, air humidity, temperature and other factors. When the rainfall rate is low, corona loss increases fast with the increase of the rainfall rate. With the increase in the rainfall rate, corona loss grows slowly. When the rainfall rate increases to some level, corona loss stop growing.
    \n\n\n
    ###
    \n\n\n
    topic: \n
    Machine learning\n
    Data models\n
    Stock markets\n
    Testing\n
    Machine learning algorithms\n
    abstract: In this paper, we provide a comparative analysis sheet of the main publicly-available benchmark data sets for stock markets statistical modelling statistical testing, providing a common language for people from different academic fields to discuss technical issues more conduct conductively. In order to more facilitate the exchange of research results of more people, this article will continue to keep up with time, and follow-up for a comprehensive study of the data model characteristics and data features of these data sets, providing a framework for statistical testing techniques and machine learning algorithms related activities of more practitioners.
    \n\n\n
    ###
    \n\n\n
    topic: \n
    Organizations\n
    Business intelligence\n
    Warehousing\n
    Data mining\n
    Decision making\n
    Databases\n
    Industries\n
    abstract: We need an effective and reliable arrangement of data and, with the foundations of statistical and business intelligence, data mining and warehousing, companies with the increased amount of data will be able to decrease uncertainty and make the best decision. In this respect, our paper overviews the concept, technology and technology trends of business intelligence, data mining and warehouse from an aspect of the infrastructure feature of the industry, classified as production planning for improving operational efficiency. In order to evaluate the benefits of using business intelligence, this paper examine some enterprises utilizing data mining and business intelligence
    \n\n\n
    '''

    TITLE_TO_ABSTRACST = '''
    write an abstract of a scientific paper using the title of the paper
    \n\n\n
    ###
    \n\n\n
    title: Research paper recommendation with topic analysis.
    \n
    abstract: With the collaborative filtering techniques becoming more and more mature, recommender systems are widely used nowadays, especially in electronic commerce and social networks. However, the utilization of recommender systems in academic research itself has not received enough attention. A research paper recommender system would greatly help researchers to find the most desirable papers in their fields of endeavour. Due to the textual nature of papers, content information could be integrated into existed recommendation methods. In this paper, we proposed that by using topic model techniques to make topic analysis on research papers, we could introduce a thematic similarity measurement into a modified version of the item-based recommendation approach. This novel recommendation method could considerably alleviate the cold start problem in research paper recommendations. Our experiment result shows that our approach could recommend highly relevant research papers.\n\n\n
    ###
    \n\n\n
    title: UHV AC corona loss measurement and analysis under the rain.\nabstract: Transmission line corona loss research is one of the critical technologies of 1000 kV UHV transmission and transformation engineering. Transmission line corona loss relates to many factors of climate, and rainfall rate affects corona loss distinctly very much. By means of UHV AC single circuit test line, corona loss monitoring and UHV corona cage conductor corona loss measurement, this paper researched the effect of rainfall rates on UHV AC single-circuit transmission lines corona loss. This paper applied a corona loss monitoring system to monitor corona loss of UHV single circuit test line and obtained corona loss monitoring data in light rain, moderate rain, and heavy rain conditions. Analyze corona loss test results. Corona loss values in light rain, moderate rain, and heavy rain conditions are obtained. The results show that rain has an obvious influence on corona loss of the line, at the beginning of rain, corona loss increases quickly, after rain, corona loss decreases with the drying of the conductor. The decay time is related to surface field strength, wind speed, air humidity, temperature and other factors. When the rainfall rate is low, corona loss increases fast with the increase of the rainfall rate. With the increase in the rainfall rate, corona loss grows slowly. When the rainfall rate increases to some level, corona loss stop growing.
    \n\n\n
    ###
    \n\n\n
    title: Cingulate circuits are associated with escalation of heroin use and naloxone-induced increases in heroin self-administration
    \n
    abstract: Opioid use disorder (OUD) is defined as a compulsion to seek and take opioids, loss of control over intake and the development of a negative emotional state when access to opioids is denied. Using functional magnetic resonance imaging (fMRI) data in a rat model of OUD, we demonstrate that the escalation of heroin self-administration (SA) and the increased heroin SA following an injection of an opioid receptor antagonist (naloxone) are associated with changes in distinct brain circuits, centered on the cingulate cortex (Cg). Here, SA escalation score was negatively associated with changes in resting state functional connectivity (rsFC) between the Cg and the dorsal striatum. Conversely, increased heroin SA following naloxone injection, was associated with increased connectivity between the Cg and the extended amygdala and hypothalamus. Naloxone-induced increased SA was also positively associated with changes in the amplitude of low frequency fluctuations within the Cg, a measure of spontaneous neuronal activity. Characterizing the distinct brain circuit and behavior changes associated with different facets of addiction increases our understanding of OUD and may provide insight into addiction prevention and treatment.
    \n\n\n
    '''
