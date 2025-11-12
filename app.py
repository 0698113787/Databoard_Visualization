import streamlit as st
import pandas as pd 
import datetime
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_excel('Adidas.xlsx')
print(df.head())

st.set_page_config(layout='wide')
st.markdown("<style>div.block-container{padding-top:1rem.}</style>",unsafe_allow_html=True)

image = Image.open('adidas_logo.webp')

col1,col2 = st.columns([0.1,0.9])
with col1:
    st.image(image,width=100)

html_title = """
  <style>
   .tile-test{
   font-weight:bold;
   padding:5x;
   border-radius:6px

   }
   </style>
   <center><h1 class ="title-test">Adidas Sales Dashboard</h1></center>"""

with col2:
    st.markdown(html_title,unsafe_allow_html=True)

col3,col4,col5 = st.columns([0.2,0.45,0.45])
with col3:
    box_date = str(datetime.datetime.now().strftime('%d %B %Y'))
    st.write(f"Last Upadated by :  \n **{box_date}**")

#lets do a barchart
with col4:

    fig = px.bar(df, x="Retailer",y="TotalSales",labels={'TotalSales':'Total Sale {R}s'},title="Total Sales By Retailers",hover_data=['TotalSales'],template='gridon',height=400)
    st.plotly_chart(fig,use_container_width=True)

_, view1,dwn1,view2,dwn2= st.columns([0.15,0.20,0.20,0.20,0.20])
with view1:
    expander = st.expander("Retailer Sales wisely")
    data = df[['Retailer','TotalSales']].groupby(by='Retailer')['TotalSales'].sum()
    expander.write(data)

#want to download data
with dwn1:
    st.download_button('Get Data',data=data.to_csv().encode('utf-8'),file_name="Retailer_sales.csv",mime="text/csv")


#wanna make line graph base on the month years i don't have month years so i will extract them from the invoceDate month and the year
df['Month_Year'] = df['InvoiceDate'].dt.strftime('%b %y')
result = df.groupby(by=df['Month_Year'])['TotalSales'].sum().reset_index()
with col5:
    fig1 = px.line(result,x='Month_Year',y='TotalSales',labels={'TotalSales':'Total Sales{R}'}, title='Total Sales Over Time', template='gridon')
    st.plotly_chart(fig1,use_container_width=True)

#i want to view the data and download it
with view2:
    expander =st.expander('Monthly Sales')
    data = result
    expander.write(data)

with dwn2:
    st.download_button('Get Data', data=result.to_csv().encode('utf-8'),file_name='Monthly Sales.csv',mime='text/csv')

#want to draw a line 
st.divider()

result1 = df.groupby(by='State')[['TotalSales','UnitsSold']].sum().reset_index()
#add the unit sold as a lime on secondary y axis like making units sold a line chart and total sales a bar chart
fig3 = go.Figure()
fig3.add_trace(go.Bar(x=result1['State'],y=result1['TotalSales'], name = 'Total Sales'))
fig3.add_trace(go.Scatter(x=result1['State'],y=result1['UnitsSold'],name='Unit sold', yaxis='y2',mode='lines'))
#update the layout to include secondary y axis
fig3.update_layout(
 title ='Total Sales And Units Sold By State',
 xaxis=dict(title='State'),
 yaxis=dict(title='Total Sales{R}'),
 yaxis2 = dict(title='Units Sold',overlaying='y',side='right',showgrid=True),
 template='gridon',
 legend = dict(x=1,y=1)

)

_, col6=st.columns([0.1,1])
with col6:
    st.plotly_chart(fig3,use_container_width=True)

#view data and download it
_,view3,dwn3=st.columns([0.5,0.45,0.45])
with view3:
    expander = st.expander('View Data For Sales By Unit Sold')
    expander.write(result1)
with dwn3:
    st.download_button('Get Data',data=result1.to_csv().encode('utf-8'),file_name='Sales_By_Unit.cs',mime='text/csv')

st.divider()

#making treemap graph now 

_,col7 = st.columns([0.1,1])
treemap = df[['Region','City','TotalSales']].groupby(by=['Region','City'])['TotalSales'].sum().reset_index()

with col7:
    fig4 = px.treemap(treemap,path=['Region','City'],values='TotalSales',hover_name='TotalSales',hover_data=['TotalSales'],color='City',height=700,width=600)
    fig4.update_traces(textinfo='label+value')
    st.subheader('Total Sales By Region And City')
    st.plotly_chart(fig4,use_container_width=True)

