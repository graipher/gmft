

# non-determinism of transformers means this might not always pass
# (ie. dependence on environment - colab/local) 



# @pytest.fixture(scope="module")
# def formatter():
#     # try out microsoft/table-transformer-structure-recognition-v1.1-all
#     config = AutoFormatConfig()
#     config.detector_path = "microsoft/table-transformer-structure-recognition-v1.1-all"
#     config.no_timm = False
#     yield AutoTableFormatter(config)



class TestCaptionBulk1:


    def test_bulk_pdf1_t0(self, pdf1_tables):
        tbl = pdf1_tables[0]
        captions = tbl.captions()
        assert captions[0] == 'Table 1 Chemicals used in diferent experiments of the study'
        assert captions[1] == '1 3' # the springer logo is detected
    def test_bulk_pdf1_t1(self, pdf1_tables):
        tbl = pdf1_tables[1]
        captions = tbl.captions()
        assert captions[0] == 'Table 2 Ranges and levels of input variables for experimental design based on CCD method'
        assert captions[1] == ''
    def test_bulk_pdf1_t2(self, pdf1_tables):
        tbl = pdf1_tables[2]
        captions = tbl.captions()
        assert captions[0] == 'Table 3 BET analysis results obtained for HCMM composite'
        assert captions[1] == '(25) S = 6 1 − 휙 dp' # some math, by subsequent
    def test_bulk_pdf1_t3(self, pdf1_tables):
        """
        This caption is to the left, not above.
        """
        tbl = pdf1_tables[3]
        captions = tbl.captions()
        assert captions[0] == 'Table 4 Results of experimental runs based on values of factors generated by experimental design'
        assert captions[1] == ''

    def test_bulk_pdf1_t4(self, pdf1_tables):
        tbl = pdf1_tables[4]
        captions = tbl.captions()
        assert captions[0] == 'Table 5 Analysis of variance of the obtained model for the response of the amount of adsorbed MB using synthesized bio-nanocomposite adsorbent'
        assert captions[1] == ''

    def test_bulk_pdf1_t5(self, pdf1_tables):
        tbl = pdf1_tables[5]
        captions = tbl.captions()
        assert captions[0] == 'Table 7 Comparison of adsorption efciency of MB in this work with other works found in the literature'
        assert captions[1] == '1 3' # springer logo

    def test_bulk_pdf1_t6(self, pdf1_tables):
        tbl = pdf1_tables[6]
        captions = tbl.captions()
        assert captions[0] == 'Table 6 Optimum conditions for achieving maximum adsorption ef\ufffeciency calculated by the aid of RSM model'
        assert captions[1] == 'Table 7 Comparison of adsorption efciency of MB in this work with other works found in the literature'
        
        # tough because Table 6 (correct) is right above, while Table 7 caption is right below
    def test_bulk_pdf1_t7(self, pdf1_tables):
        tbl = pdf1_tables[7]
        captions = tbl.captions()
        assert captions[0] == 'Table 8 Predicted values of the parameters of Langmuir, Freundlich, Temkin, and D–R isotherm models for the adsorption of MB dye using HCMM adsorbent'
        assert captions[1] == ''

    def test_bulk_pdf1_t8(self, pdf1_tables):
        tbl = pdf1_tables[8]
        captions = tbl.captions()
        assert captions[0] == 'Table 9 Calculated parameters of diferent kinetic models based on experimental data for MB adsorption on HCMM composite'
        assert captions[1] == 'Conclusions' # proximal; below

    # def test_bulk_pdf1_t9(self, pdf1_tables):
    #     pass
    


class TestCaptionBulk2:
    
    

    def test_bulk_pdf2_t0(self, pdf2_tables):
        tbl = pdf2_tables[0]
        captions = tbl.captions()
        assert captions[0] == 'Table 1 Stages of population pharmacokinetic analysis'
        assert captions[1] == 'BID twice daily, TID three times daily'
    def test_bulk_pdf2_t1(self, pdf2_tables):
        """
        This caption is to the left, not above.
        """
        
        tbl = pdf2_tables[1]
        captions = tbl.captions()
        assert captions[0] == 'Table 2 Demographics and baseline characteristics for the pharmacokinetic analysis subject population (n = 34)'
        assert captions[1] == 'a eGFR using the CKD-EPI cystatin C equation[19]' # a eGFR using the CKD-EPI cystatin C equation[19]
    def test_bulk_pdf2_t2(self, pdf2_tables):
        tbl = pdf2_tables[2]
        captions = tbl.captions()
        assert captions[0] == 'Table 3 Summary statistics for Css,ave in ng/mL for various ManNAc dosing regimens in subjects with GNE myopathy (N = 90)'
        assert captions[1] == 'Dosing regimens: Q8H every 8 h, Q12H every 12 hours, Q24H once daily Css,ave average drug concentration at steady state'

    def test_bulk_pdf2_t3(self, pdf2_tables):
        tbl = pdf2_tables[3]
        captions = tbl.captions()
        assert captions[0] == 'Table 4 Final population pharmacokinetic model parameter estimates for ManNAc and Neu5Ac in subjects with GNE myopathy'
        assert captions[1] == ''


class TestCaptionBulk3:

    # def test_bulk_pdf3_t0(self, pdf3_tables):
    #     pass
        # tbl = pdf3_tables[0]
        # captions = tbl.captions()

    def test_bulk_pdf3_t1(self, pdf3_tables):
        tbl = pdf3_tables[1]
        captions = tbl.captions()
        assert captions[0] == 'Table 1 | DFT calculated BE of neutral diaryl intermediates for \
transalkylation (Itrans) and disproportionation (Idisp) in zeolites \
with different microporous structure'
        # assert captions[1] == ''  # false positive: paragraph below (proximal)
    def test_bulk_pdf3_t2(self, pdf3_tables):
        tbl = pdf3_tables[2]
        captions = tbl.captions()
        assert captions[0] == 'Table 2 | Calculated activation barriers (in kJ/mol) for all the elementary steps of the transalkylation and disproportiona\ufffetion mechanisms in different zeolite structures'
        # assert captions[1] == '' # false positive: paragraph below (proximal)

    def test_bulk_pdf3_t3(self, pdf3_tables):
        tbl = pdf3_tables[3]
        captions = tbl.captions()
        assert captions[0] == 'Table 3 | Results of catalytic test in diethylbenzene-benzene transalkylation at 240 °C'
        assert captions[1] == 'a Calculated using the Arrhenius equation.'


class TestCaptionBulk4:

    # def test_bulk_pdf4_t0(self, pdf4_tables):
    #     tbl = pdf4_tables[0]
    #     captions = tbl.captions()
    #     assert captions[0] == ''
    #     assert captions[1] == ''

        #Figure 2. Overview of all identified statistically significant associations. (a) In the figure, each node is ...
        # this caption is very long
    def test_bulk_pdf4_t1(self, pdf4_tables):
        tbl = pdf4_tables[1] # ONLY example of caption below
        captions = tbl.captions()
        assert captions[0] == 'www.nature.com/scientificreports/' # logo - debatable
        assert captions[1] == 'Table 1. Summary of integrated data. ER, PR and HER2 refer to Estrogen Receptor, Progesterone Receptor, and Human Epidermal growth factor Receptor 2, respectively.'


class TestCaptionBulk5:

    def test_bulk_pdf5_t0(self, pdf5_tables):
        tbl = pdf5_tables[0]
        captions = tbl.captions(line_spacing=3)
        assert captions[0] == 'Table 1 \
SF-ROX data-processing and refinement statistics. \
Values in parentheses are for the highest resolution shell.'
        assert captions[1] == '† Rsplit is as defined by White et al. (2013). ‡ The correlation coefficient between half \
data sets is as defined by Karplus & Diederichs (2015).'

    def test_bulk_pdf5_t1(self, pdf5_tables):
        tbl = pdf5_tables[1]
        captions = tbl.captions(line_spacing=3)
        assert captions[0] == 'Table 2 \
Neutron data-processing and refinement statistics for neutronOX. \
Values in parentheses are for the highest resolution shell.'
        assert captions[1] == ''

class TestCaptionBulk6:

    def test_bulk_pdf6_t0(self, pdf6_tables):
        tbl = pdf6_tables[0]
        captions = tbl.captions()
        assert captions[0] == 'Table 1 Agronomic traits of test materials at maturity in 2019 and 2020'
        assert captions[1] == 'T0, control group with no removing-spikelets; T1, removing top 2/3 of the spikelets in panicle; SG, superior spikelets located on all primary branches of rice panicle; \
IG, inferior spikelets located on all secondary branches of rice panicle; Diferent letters indicate statistically signifcant diferences under the same year at the P=0.05 \
level; The data are the means of three replications±SD, consisting of 30 plants each'
        # this is actually the correct bottom caption

    def test_bulk_pdf6_t1(self, pdf6_tables):
        tbl = pdf6_tables[1]
        captions = tbl.captions()
        assert captions[0] == 'Table 2 Diferential sensitivity of photosynthesis in fag leaves to remove spikelets in CJ03 and W1844 at 8 DPA in 2019 and 2020'
        assert captions[1] == 'T0, control group with no removing-spikelets; T1, removing top 2/3 of the spikelets in panicle; Diferent letters indicate statistically signifcant diferences under the \
same year at the P=0.05 level; The data are the means of three replications±SD, consisting of 9 plants each'
        # also correct caption
        
    def test_bulk_pdf6_t2(self, pdf6_tables):
        tbl = pdf6_tables[2]
        captions = tbl.captions()
        assert captions[0] == 'Abbreviations'
        assert captions[1] == ''


class TestCaptionBulk7:

    def test_bulk_pdf7_t0(self, pdf7_tables):
        tbl = pdf7_tables[0]
        captions = tbl.captions()
        assert captions[0] == 'Table 1 Virological and clinical characteristics of patients with hepatitis C virus infection'
        assert captions[1] == 'a SVR, sustained virologic response; non-SVR, no sustained virologic response'

    def test_bulk_pdf7_t1(self, pdf7_tables):
        tbl = pdf7_tables[1]
        captions = tbl.captions() # stop_y_factor_below=17.5)
        assert captions[0] == 'Table 2 Host and viral baseline parameters in patients with and without treatment response'
        assert captions[1] == 'a Mann-Whitney U test. \
b Fisher’s exact test. \
c Fibrosis was scored according to Ludwig and Batts, and was available for 34 patients. \
d Logistic regression. \
e Chi square test.'
    def test_bulk_pdf7_t2(self, pdf7_tables):
        tbl = pdf7_tables[2]
        captions = tbl.captions()
        assert captions[0] == 'Table 3 Distribution of amino acids at residue 70 and 91 of the core region'
        assert captions[1] == 'A total of 3317 sequences found on 31st of March 2010 in the The Hepatitis C \
Virus (HCV) Database Project (http://hcv.lanl.gov/) were analysed. Values less \
than 1% not shown.'


# class TestCaptionBulk8:

#     def test_bulk_pdf8_t0(self, pdf8_tables):
#         pass
#         # rot. table
#         # tbl = pdf8_tables[0]
#         # captions = tbl.captions()
#         assert captions[0] == ''
#         assert captions[1] == ''

# #     def test_bulk_pdf8_t1(self, pdf8_tables):
# #         tbl = pdf8_tables[1]
# #         captions = tbl.captions()
#         assert captions[0] == 'Table 2 \
# # Compilation of experiments performed assessing water solubility in silicate melts at low total pressures over a range of temperatures and compositions. NB. The value of \
# # αH2O is calculated on the basis of mole fraction rather than ppmw'
#         assert captions[1] == ''

    

