import streamlit as st
from PIL import Image
import streamlit.components.v1 as components

# Custom CSS for stylish design
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700&display=swap');
    body {
        background-color: #FFFFFF;
        color: #333;
    }
    .main-title {
        font-family: 'Montserrat', sans-serif;
        font-size: 3em;
        color: #2E4053;
        text-align: center;
        margin-bottom: 20px;
    }
    .highlight {
        font-family: 'Arial', sans-serif';
        font-size: 2em;
        font-weight: bold;
        color: #3498DB;
        text-align: center;
        margin: 20px 0;
    }
    .bold-number {
        font-size: 3em;
        color: #E74C3C;
    }
    .quote {
        font-family: 'Georgia', serif;
        font-size: 1.3em;
        font-style: italic;
        color: #7D3C98;
        margin-top: 30px;
        text-align: center;
    }
    .section-title {
        font-family: 'Verdana', sans-serif;
        font-size: 1.5em;
        color: #2874A6;
        margin-top: 20px;
        text-align: center;
    }
    .info-box {
        background-color: #3498DB;
        color: #FFFFFF;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        text-align: center;
    }
    .stats-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin-top: 20px;
    }
    .stat-box {
        background-color: #F2F4F4;
        color: #333;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        width: 80%;
        text-align: center;
    }
    .stat-title {
        font-size: 1.5em;
        color: #2E4053;
    }
    .stat-value {
        font-size: 2.5em;
        color: #E74C3C;
        font-weight: bold;
    }
    .tableauPlaceholder {
        margin: 0 auto;
        padding: 0;
    }
    .streamlit-expanderHeader {
        font-size: 1.5em;
        color: #2E4053;
    }
    .call-button, .email-button {
        display: inline-block;
        margin: 5px;
        padding: 10px;
        background-color: #3498DB;
        color: #FFF;
        text-decoration: none;
        border-radius: 5px;
    }
    .call-button::before, .email-button::before {
        content: '';
        margin-right: 5px;
        display: inline-block;
        vertical-align: middle;
    }
    .call-button::before {
        content: '📞';
    }
    .email-button::before {
        content: '📧';
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for navigation
st.sidebar.title("Navigation")
pages = [
    "Introduction",
    "Shocking Facts About Lung Cancer",
    "Demographics",
    "Symptoms",
    "Causes",
    "Recommendations",
    "Initiatives",
    "Risk Assessment",
    "Upcoming Campaigns",
    "Public Blog"
]
selection = st.sidebar.radio("Go to", pages)

if selection == "Introduction":
    st.markdown("<div class='main-title' style='color: #C0392B;'>Lung Cancer: A Silent Killer</div>", unsafe_allow_html=True)
    st.markdown("""
        <div style='font-size: 1.5em; color: #2E4053; text-align: center; margin-top: 20px; font-family: Arial, sans-serif;'>
            "Lung cancer silently invades lives, but through awareness and early action, we can turn the tide. Your knowledge and action today can save lives tomorrow."
        </div>
        <div style='font-size: 1.2em; color: #2E4053; margin-top: 40px; text-align: center;'>
        </div>
        <div style='font-family: Montserrat, sans-serif; font-size: 2em; color: #2980B9; text-align: center; margin-top: 40px;'>
        </div>
        <div style='font-family: Montserrat, sans-serif; font-size: 2em; color: #2980B9; text-align: center; margin-top: 40px;'>
            Join the Fight Against Lung Cancer
        </div>
        <div style='font-size: 1.2em; color: #2E4053; margin-top: 20px; text-align: center; line-height: 1.6;'>
            By raising awareness and educating the community, we can reduce the incidence of lung cancer and support those who are battling this devastating disease. Together, we can make a difference.
        </div>
    """, unsafe_allow_html=True)





elif selection == "Shocking Facts About Lung Cancer":
    st.markdown("<div class='main-title' style='font-family: Verdana, sans-serif; font-size: 3.5em; color: #E74C3C;'>Shocking Facts About Lung Cancer</div>", unsafe_allow_html=True)
    st.markdown("""
        <div class='stats-container'>
            <div class='stat-box'>
                <div class='stat-title'>Leading Cause of Cancer-Related Deaths</div>
                <div class='stat-value'>#1</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>Second Most Commonly Diagnosed Cancer</div>
                <div class='stat-value'>#2</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>New Cases Reported in 2022</div>
                <div class='stat-value'>2.5 Million</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>Percentage of All Cancer Cases</div>
                <div class='stat-value'>12.4%</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>Cancer-Related Deaths Globally</div>
                <div class='stat-value'>1.8 Million</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>Percentage of Cancer-Related Deaths</div>
                <div class='stat-value'>18.7%</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>Most Common Cancer in Men</div>
                <div class='stat-value'>#1</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>Second Most Common Cancer in Women</div>
                <div class='stat-value'>#2</div>
            </div>
            <div class='stat-box'>
                <div class='stat-title'>High Mortality Rate Due to Late-Stage Diagnosis</div>
                <div class='stat-value'>High</div>
            </div>
        </div>
    """, unsafe_allow_html=True)

elif selection == "Demographics":
    st.markdown("<div class='main-title'>The Demographics of Lung Cancer</div>", unsafe_allow_html=True)
    st.subheader('Interactive Tableau Dashboard')
    tableau_embed_code = """
    <div class='tableauPlaceholder' id='viz1718029443075' style='position: relative; width: 1500px; height: 1500px;'>
        <noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Lu&#47;LungCancer-ManouellaHelou&#47;DemographicDashboard&#47;1_rss.png' style='border: none' /></a></noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='LungCancer-ManouellaHelou&#47;DemographicDashboard' />
            <param name='tabs' value='yes' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Lu&#47;LungCancer-ManouellaHelou&#47;DemographicDashboard&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1718029443075');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if ( divElement.offsetWidth > 800 ) {
            vizElement.style.minWidth='1500px';
            vizElement.style.maxWidth='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        } else if ( divElement.offsetWidth > 500 ) {
            vizElement.style.minWidth='1500px';
            vizElement.style.maxWidth='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        } else {
            vizElement.style.width='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """
    components.html(tableau_embed_code, height=1100, width=1500)
    st.markdown("""
        The dashboard provides a comprehensive overview of lung cancer demographics:
        - **Geographical Distribution**: The USA leads in lung cancer cases with over 7.7 million, followed by significant numbers in the UK, Japan, and Italy. This highlights the need for targeted public health initiatives in these regions.
        - **Gender Trends**: Historically, males have had higher lung cancer rates than females. However, the gap is narrowing, possibly due to changes in smoking patterns and occupational exposures.
        - **Age Distribution**: Lung cancer incidence increases with age, peaking between 75 and 80 years. This emphasizes the importance of early detection and preventive measures, particularly for older adults.
        - **Top 15 Countries**: The highest cases are found in developed countries, indicating potential links with lifestyle factors and environmental exposures.

        Understanding these patterns helps in designing effective prevention, early detection, and treatment strategies.
    """, unsafe_allow_html=True)

elif selection == "Symptoms":
    st.markdown("<div class='main-title'>Symptoms of Lung Cancer</div>", unsafe_allow_html=True)
    st.subheader('Interactive Tableau Dashboard')
    tableau_embed_code = """
    <div class='tableauPlaceholder' id='viz1718029328216' style='position: relative; width: 1500px; height: 1500px;'>
        <noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;G9&#47;G9H88GNWH&#47;1_rss.png' style='border: none' /></a></noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='path' value='shared&#47;G9H88GNWH' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;G9&#47;G9H88GNWH&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1718029328216');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if ( divElement.offsetWidth > 800 ) {
            vizElement.style.minWidth='1500px';
            vizElement.style.maxWidth='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        } else if ( divElement.offsetWidth > 500 ) {
            vizElement.style.minWidth='1500px';
            vizElement.style.maxWidth='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        } else {
            vizElement.style.width='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """
    components.html(tableau_embed_code, height=1500, width=1500)
    st.markdown("""
        The dashboard provides an overview of lung cancer symptoms:
        - **Dry Cough**: Severity increases with the progression of lung cancer.
        - **Fatigue Level**: Higher cancer levels correlate with increased fatigue.
        - **Wheezing**: 36.5% of patients with high cancer levels experience wheezing, 33.2% with moderate cancer levels, and 30.3% with low cancer levels.
        - **Swallowing Difficulty**: More prevalent at higher cancer levels.
        - **Shortness of Breath**: Increases with higher cancer levels.
        - **Clubbing of Fingernails**: 36.5% of patients with high cancer levels experience clubbing, 33.2% with moderate levels, and 30.3% with low levels.
        - **Coughing of Blood**: High levels of coughing blood are predominant in advanced cancer cases.
        
        Understanding these symptoms helps in early detection and management of lung cancer.
    """, unsafe_allow_html=True)

elif selection == "Causes":
    st.markdown("<div class='main-title'>Main Causes of Lung Cancer</div>", unsafe_allow_html=True)
    st.subheader('Interactive Tableau Dashboard')
    tableau_embed_code = """
    <div class='tableauPlaceholder' id='viz1718028554004' style='position: relative; width: 1500px; height: 1500px;'>
        <noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Lu&#47;LungCancer-ManouellaHelou&#47;CausesofLungCancer&#47;1_rss.png' style='border: none' /></a></noscript>
        <object class='tableauViz' style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' />
            <param name='embed_code_version' value='3' />
            <param name='site_root' value='' />
            <param name='name' value='LungCancer-ManouellaHelou&#47;CausesofLungCancer' />
            <param name='tabs' value='yes' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Lu&#47;LungCancer-ManouellaHelou&#47;CausesofLungCancer&#47;1.png' />
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
        </object>
    </div>
    <script type='text/javascript'>
        var divElement = document.getElementById('viz1718028554004');
        var vizElement = divElement.getElementsByTagName('object')[0];
        if ( divElement.offsetWidth > 800 ) {
            vizElement.style.minWidth='1500px';
            vizElement.style.maxWidth='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        } else if ( divElement.offsetWidth > 500 ) {
            vizElement.style.minWidth='1500px';
            vizElement.style.maxWidth='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        } else {
            vizElement.style.width='100%';
            vizElement.style.minHeight='1500px';
            vizElement.style.maxHeight='1500px';
        }
        var scriptElement = document.createElement('script');
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';
        vizElement.parentNode.insertBefore(scriptElement, vizElement);
    </script>
    """
    components.html(tableau_embed_code, height=1200, width=1500)

    st.markdown("""
        The dashboard provides an in-depth analysis of the main causes of lung cancer:
        - **Air Pollution**: High levels of air pollution are strongly associated with increased lung cancer cases. Medium and low pollution levels also contribute to lung cancer but to a lesser extent. This indicates a clear link between air quality and lung cancer risk, emphasizing the need for stringent air pollution control measures.
        - **Smoking**: Both active smoking and passive smoking (secondhand smoke) are significant risk factors for lung cancer. As the smoking level increases from low to high, there is a corresponding increase in lung cancer cases. This correlation underscores the importance of anti-smoking campaigns and smoking cessation programs to reduce lung cancer incidence.
        - **Alcohol**: High levels of alcohol consumption are associated with higher cancer levels, indicating that excessive alcohol intake may contribute to lung cancer risk. This suggests that public health strategies should also address alcohol consumption as part of lung cancer prevention efforts.
        - **Obesity**: Both moderate and high levels of obesity are associated with increased lung cancer risk. This connection suggests that maintaining a healthy weight through diet and exercise could be an essential factor in reducing lung cancer risk.
        - **Genetic Risk**: Individuals with a family history of lung cancer (genetic predisposition) have a higher likelihood of developing the disease. High genetic risk is particularly associated with lung cancer cases, highlighting the importance of genetic counseling and regular screening for individuals with a family history of lung cancer.
        
        Understanding these causes helps in designing targeted interventions and public health policies to prevent lung cancer.
    """, unsafe_allow_html=True)
elif selection == "Recommendations":
    st.markdown("<div class='main-title'>Recommendations to Prevent Lung Cancer</div>", unsafe_allow_html=True)

    st.markdown("### Government")
    st.markdown("""
        - **Implement Strict Anti-Smoking Laws**: Enforce comprehensive laws that prohibit smoking in all public places, including restaurants, bars, and workplaces. Increase taxes on tobacco products to discourage smoking and use the revenue to fund public health programs.
        - **Air Quality Regulations**: Develop stringent regulations to control emissions from industrial facilities, vehicles, and other sources of air pollution. Implement monitoring systems to ensure compliance and penalize violators.
        - **Public Awareness Campaigns**: Launch nationwide campaigns using various media channels to educate the public about the risks of smoking, secondhand smoke, and air pollution. Include testimonials from lung cancer survivors to emphasize the message.
        - **Support for Research**: Allocate funds for research on lung cancer prevention, early detection, and treatment. Encourage public and private partnerships to accelerate the development of new technologies and therapies.
        - **Healthcare Access**: Ensure that all citizens have access to affordable healthcare services, including lung cancer screenings and treatments. Implement policies that support early detection and continuous care for cancer patients.
    """)

    st.markdown("### People")
    st.markdown("""
        - **Quit Smoking**: If you smoke, seek help to quit through support groups, cessation programs, and nicotine replacement therapies. Utilize resources like hotlines, mobile apps, and online communities for support.
        - **Reduce Alcohol Consumption**: Limit alcohol intake to lower your overall cancer risk. Follow guidelines for moderate drinking and avoid binge drinking.
        - **Avoid Secondhand Smoke**: Make your home and car smoke-free zones. Politely ask others not to smoke around you, especially in enclosed spaces.
        - **Maintain a Healthy Lifestyle**: Adopt a balanced diet rich in fruits, vegetables, and whole grains. Engage in regular physical activity and maintain a healthy weight to boost your immune system and reduce cancer risk.
        - **Get Regular Check-Ups**: Schedule annual health check-ups and discuss lung cancer screenings with your healthcare provider, especially if you are at high risk due to smoking or family history.
        - **Reduce Exposure to Air Pollution**: Use air purifiers at home, avoid outdoor activities during high pollution days, and support clean energy initiatives in your community.
    """)

    st.markdown("### Influencers")
    st.markdown("""
        - **Raise Awareness**: Use your social media platforms to educate your followers about the dangers of smoking and air pollution. Share factual information, personal stories, and resources for quitting smoking.
        - **Promote Healthy Choices**: Advocate for healthy lifestyles by sharing tips on quitting smoking, reducing alcohol consumption, and maintaining a healthy diet and exercise routine.
        - **Collaborate with Health Organizations**: Partner with health organizations and campaigns to amplify messages about lung cancer prevention. Participate in public health events and fundraisers.
        - **Create Engaging Content**: Develop engaging content such as videos, blog posts, and infographics that highlight the importance of lung cancer prevention and early detection.
    """)

    st.markdown("### Companies")
    st.markdown("""
        - **Create Smoke-Free Workplaces**: Implement and strictly enforce a smoke-free policy within all company premises, including designated smoking areas.
        - **Support Employee Wellness**: Offer comprehensive wellness programs that include smoking cessation support, stress management, and health education. Provide incentives for employees to participate.
        - **Reduce Emissions**: Invest in green technologies and adopt practices that minimize air pollution. Comply with environmental regulations and strive for sustainability in all operations.
        - **Corporate Social Responsibility**: Fund or participate in public health campaigns and lung cancer research. Sponsor events and initiatives that promote a healthy lifestyle and environment.
        - **Health Benefits**: Ensure that employee health benefits cover lung cancer screenings and treatments. Promote preventive healthcare measures among employees.
    """)

    st.markdown("### Hospitals")
    st.markdown("""
        - **Screening Programs**: Implement regular lung cancer screening programs, especially targeting high-risk individuals such as smokers and those with a family history of lung cancer. Use advanced screening technologies to improve early detection rates.
        - **Patient Education**: Provide comprehensive education to patients about the risks of smoking, secondhand smoke, and air pollution. Offer resources and support for smoking cessation.
        - **Support Groups**: Establish and promote support groups for patients and families affected by lung cancer. Facilitate peer support and provide psychological counseling.
        - **Collaborate on Research**: Partner with academic institutions and research organizations to advance the understanding of lung cancer prevention and treatment. Participate in clinical trials and share findings with the broader medical community.
        - **Community Outreach**: Engage in community outreach programs to raise awareness about lung cancer. Conduct free screening events and educational workshops in underserved areas.
    """)

    st.markdown("### Doctors")
    st.markdown("""
        - **Advise Patients on Risk Factors**: Proactively counsel patients on the risks associated with smoking, alcohol consumption, and air pollution. Provide practical advice and resources for quitting smoking and reducing exposure to pollutants.
        - **Promote Regular Screenings**: Encourage patients, particularly those at high risk, to undergo regular lung cancer screenings. Discuss the benefits and potential outcomes of early detection.
        - **Stay Informed**: Keep abreast of the latest research and advancements in lung cancer prevention, diagnosis, and treatment. Attend medical conferences and participate in continuing education.
        - **Advocate for Public Health**: Use your professional influence to support public health initiatives aimed at reducing lung cancer risk. Collaborate with local health departments and advocacy groups.
        - **Personalized Care**: Offer personalized care plans that address the specific needs and risk factors of each patient. Monitor their progress and adjust recommendations as needed.
    """)


elif selection == "Initiatives":
    st.markdown("<div class='main-title'>Lung Cancer Prevention Initiatives</div>", unsafe_allow_html=True)
    
    with st.expander("Smoking and Alcohol Cessation Programs"):
        st.markdown("""
        Online programs that help people quit smoking:
        - [Smokefree.gov](https://smokefree.gov/): Provides resources and support to help people quit smoking, including quit plans, tips, and tools.
        - [BecomeAnEX](https://www.becomeanex.org/): Offers a free quit plan, expert guidance, and a supportive community to help users quit smoking.
        - [Quit.org](https://www.quit.org/): Provides information, resources, and support to help people quit smoking and stay smoke-free.
        - [My Drinkaware](https://www.drinkaware.co.uk/tools/my-drinkaware): A personal tool to track alcohol consumption and receive tips for cutting down.
        - [Alcohol Change UK](https://alcoholchange.org.uk/help-and-support/get-help-now): Offers resources and support for reducing alcohol consumption and leading a healthier life.
        """)

    with st.expander("Educational Content on Health Risks of Smoking and Alcohol"):
        st.markdown("""
        Smoking and alcohol consumption significantly increase the risk of developing lung cancer and other health issues. Some key points include:
        - **Smoking**: 
          - Causes about 85% of lung cancer cases.
          - Secondhand smoke also increases the risk of lung cancer.
          - Contains over 7,000 chemicals, at least 69 of which are known to cause cancer.
        - **Alcohol**: 
          - Consumption is linked to a higher risk of developing cancer, including lung cancer.
          - Heavy drinking can weaken the body's ability to fight off diseases and infections.
        - **Combining Smoking and Alcohol**:
          - Increases cancer risk more than either factor alone.
          - Greater impact on organs such as the lungs, liver, and throat.

        It is crucial to educate the public about these risks to promote healthier lifestyle choices.
        """)

    with st.expander("Programs to Reduce Air Pollution"):
        st.markdown("""
        Promoting programs that reduce air pollution is essential in the fight against lung cancer. Contact these organizations to get involved:
        - **Environmental Protection Agency (EPA)**: 
          - How it helps: The EPA develops and enforces regulations that protect the air quality.
          - [📞 Call EPA](https://www.epa.gov/contact-epa)
          - [📧 Email EPA](mailto:epa@epa.gov)
        - **Clean Air Task Force**: 
          - How it helps: This organization advocates for policies and technologies that reduce air pollution.
          - [📞 Call Clean Air Task Force](https://www.catf.us/contact/)
          - [📧 Email Clean Air Task Force](mailto:info@catf.us)
        - **Global Alliance for Clean Cookstoves**: 
          - How it helps: This alliance promotes clean cooking solutions to reduce household air pollution.
          - [📞 Call Clean Cooking Alliance](https://www.cleancookingalliance.org/contact/)
          - [📧 Email Clean Cooking Alliance](mailto:info@cleancookingalliance.org)
        """)

elif selection == "Risk Assessment":
    st.markdown("<div class='main-title'>Lung Cancer Risk Assessment</div>", unsafe_allow_html=True)
    st.markdown("Select your level of symptoms and causes (1 to 8) to assess your lung cancer risk.")

    symptoms = {
        "Dry Cough": st.slider("Dry Cough", 1, 8, 1),
        "Fatigue Level": st.slider("Fatigue Level", 1, 8, 1),
        "Wheezing": st.slider("Wheezing", 1, 8, 1),
        "Swallowing Difficulty": st.slider("Swallowing Difficulty", 1, 8, 1),
        "Shortness of Breath": st.slider("Shortness of Breath", 1, 8, 1),
        "Clubbing of Fingernails": st.slider("Clubbing of Fingernails", 1, 8, 1),
        "Coughing of Blood": st.slider("Coughing of Blood", 1, 8, 1)
    }

    causes = {
        "Air Pollution": st.slider("Air Pollution", 1, 8, 1),
        "Smoking": st.slider("Smoking", 1, 8, 1),
        "Alcohol": st.slider("Alcohol", 1, 8, 1),
        "Obesity": st.slider("Obesity", 1, 8, 1),
        "Genetic Risk": st.slider("Genetic Risk", 1, 8, 1)
    }

    risk_score = sum(symptoms.values()) + sum(causes.values())
    if risk_score < 30:
        risk_level = "Low"
    elif 30 <= risk_score < 60:
        risk_level = "Medium"
    else:
        risk_level = "High"

    st.markdown(f"Your assessed lung cancer risk level is: **{risk_level}**")

elif selection == "Upcoming Campaigns":
    st.markdown("<div class='main-title'>Upcoming Lung Cancer Awareness Campaigns</div>", unsafe_allow_html=True)
    st.markdown("""
        **Awareness Campaign Schedule in Lebanon:**

        - **Beirut Awareness Rally**: 
          - Date: 15th June 2024
          - Location: Martyrs' Square
          - Activities:
            - **09:00 - 10:00 Registration and Welcome**: Meet and greet, pick up your rally materials, and enjoy some light refreshments.
            - **10:00 - 12:00 Health Check-ups and Screenings**: Free lung health screenings provided by medical professionals.
            - **12:00 - 14:00 Educational Workshops**: Interactive sessions on lung cancer prevention, symptoms, and treatment options.
            - **14:00 - 16:00 Anti-Smoking Pledges**: Public pledges to quit smoking, with support and resources available on-site.
            - **16:00 - 18:00 Awareness March**: Join us for a march through downtown Beirut to raise awareness about lung cancer.
            - **18:00 - 19:00 Closing Remarks**: Inspirational speeches from lung cancer survivors and healthcare professionals.

        - **Tripoli Health Fair**:
          - Date: 20th June 2024
          - Location: Al-Tal Square
          - Activities:
            - **09:00 - 10:00 Registration and Welcome**: Pick up your fair materials and enjoy some breakfast snacks.
            - **10:00 - 12:00 Public Speeches**: Hear from experts and advocates about the latest in lung cancer research and treatment.
            - **12:00 - 14:00 Distribution of Educational Pamphlets**: Learn more about lung cancer prevention and treatment.
            - **14:00 - 16:00 Community Discussions**: Join small group discussions led by health professionals on various topics related to lung cancer.
            - **16:00 - 18:00 Q&A with Experts**: Get your questions answered by top lung cancer experts.
            - **18:00 - 19:00 Closing Remarks**: Final thoughts and a look ahead to future initiatives.

        - **Sidon Wellness Walk**:
          - Date: 25th June 2024
          - Location: Sidon Sea Castle
          - Activities:
            - **09:00 - 10:00 Registration and Welcome**: Collect your walk materials and enjoy a healthy breakfast.
            - **10:00 - 12:00 Awareness Walk**: Join us for a scenic walk along the coast to promote lung health.
            - **12:00 - 14:00 Health Consultations**: Free consultations with lung health specialists.
            - **14:00 - 16:00 Interactive Sessions on Smoking Dangers**: Learn about the risks of smoking and how to quit.
            - **16:00 - 18:00 Smoke-Free Environment Activities**: Participate in activities promoting a smoke-free lifestyle.
            - **18:00 - 19:00 Closing Remarks**: Hear from community leaders and health experts.

        - **Zahle Health Expo**:
          - Date: 30th June 2024
          - Location: Zahle Boulevard
          - Activities:
            - **09:00 - 10:00 Registration and Welcome**: Start your day with a welcome from local officials and health advocates.
            - **10:00 - 12:00 Lung Health Screening**: Free lung screenings and consultations.
            - **12:00 - 14:00 Expert Talks**: Presentations by leading researchers and doctors on the latest in lung cancer treatment.
            - **14:00 - 16:00 Community Engagement Activities**: Participate in activities designed to educate and engage the community on lung health.
            - **16:00 - 18:00 Latest Advancements in Treatment**: Learn about the newest treatments and technologies in lung cancer care.
            - **18:00 - 19:00 Closing Remarks**: Inspirational messages and a call to action from health leaders.

        Join us in these campaigns to spread awareness and promote lung health across Lebanon.
    """)

    st.markdown("<div class='main-title'>Register for the Campaign</div>", unsafe_allow_html=True)
    name = st.text_input("Name")
    family_name = st.text_input("Family Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    phone_number = st.text_input("Phone Number")
    email_address = st.text_input("Email Address")
    campaign_name = st.multiselect("Campaign Name", ["Beirut Awareness Rally", "Tripoli Health Fair", "Sidon Wellness Walk", "Zahle Health Expo"])

    if st.button("Register"):
        st.success("Thank you for registering!")

elif selection == "Public Blog":
    st.markdown("<div class='main-title'>Public Blog on Air Pollution</div>", unsafe_allow_html=True)
    st.markdown("""
        **Share your experiences and observations about air pollution in your city. Your voice can help put pressure on the government to implement stricter air quality regulations.**

        **Example Posts:**

        **John Doe from Beirut**
        *"The air quality in my neighborhood has been deteriorating rapidly. We need immediate action!"* 
        👍 120  👎 10

        **Jane Smith from Tripoli**
        *"My children are experiencing respiratory issues due to the pollution. This needs to stop!"*
        👍 200  👎 5

        **Ahmad Karam from Sidon**
        *"The government must address the air pollution in our city. It's affecting everyone's health!"*
        👍 300  👎 20

        **Sara Haddad from Zahle**
        *"Air pollution levels are getting worse. We need stricter regulations and cleaner air now!"*
        👍 150  👎 8

        **Michael Habib from Jounieh**
        *"The smog over our city is unbearable. Government action is overdue!"*
        👍 180  👎 15

        **Leila Nassif from Baalbek**
        *"Factories are polluting our air and making us sick. We demand better air quality!"*
        👍 220  👎 12
    """)

    st.markdown("<div class='main-title'>Your Post</div>", unsafe_allow_html=True)
    name = st.text_input("Name", key="blog_name")
    message = st.text_area("Message", key="blog_message")
    image = st.file_uploader("Upload your image", type=["png", "jpg", "jpeg"], key="blog_image")

    if st.button("Submit", key="blog_submit"):
        st.success("Thank you for your post!")
