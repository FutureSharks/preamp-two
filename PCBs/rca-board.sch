<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="6.6.0">
<drawing>
<settings>
<setting alwaysvectorfont="yes"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="2" name="Route2" color="1" fill="3" visible="no" active="no"/>
<layer number="3" name="Route3" color="4" fill="3" visible="no" active="no"/>
<layer number="4" name="Route4" color="1" fill="4" visible="no" active="no"/>
<layer number="5" name="Route5" color="4" fill="4" visible="no" active="no"/>
<layer number="6" name="Route6" color="1" fill="8" visible="no" active="no"/>
<layer number="7" name="Route7" color="4" fill="8" visible="no" active="no"/>
<layer number="8" name="Route8" color="1" fill="2" visible="no" active="no"/>
<layer number="9" name="Route9" color="4" fill="2" visible="no" active="no"/>
<layer number="10" name="Route10" color="1" fill="7" visible="no" active="no"/>
<layer number="11" name="Route11" color="4" fill="7" visible="no" active="no"/>
<layer number="12" name="Route12" color="1" fill="5" visible="no" active="no"/>
<layer number="13" name="Route13" color="4" fill="5" visible="no" active="no"/>
<layer number="14" name="Route14" color="1" fill="6" visible="no" active="no"/>
<layer number="15" name="Route15" color="4" fill="6" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="pinhead">
<description>&lt;b&gt;Pin Header Connectors&lt;/b&gt;&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="1X03">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-3.175" y1="1.27" x2="-1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="1.27" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-0.635" x2="-1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="1.27" x2="0.635" y2="1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="1.27" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-0.635" x2="0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="0.635" y1="-1.27" x2="-0.635" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-0.635" y1="-1.27" x2="-1.27" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="-3.175" y1="1.27" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="-0.635" x2="-3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="-1.905" y1="-1.27" x2="-3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="1.905" y2="1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="1.27" x2="3.175" y2="1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="1.27" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="3.81" y2="-0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-0.635" x2="3.175" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="3.175" y1="-1.27" x2="1.905" y2="-1.27" width="0.1524" layer="21"/>
<wire x1="1.905" y1="-1.27" x2="1.27" y2="-0.635" width="0.1524" layer="21"/>
<pad name="1" x="-2.54" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="0" y="0" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="2.54" y="0" drill="1.016" shape="long" rot="R90"/>
<text x="-3.8862" y="1.8288" size="1.27" layer="25" ratio="10">&gt;NAME</text>
<text x="-3.81" y="-3.175" size="1.27" layer="27">&gt;VALUE</text>
<rectangle x1="-0.254" y1="-0.254" x2="0.254" y2="0.254" layer="51"/>
<rectangle x1="-2.794" y1="-0.254" x2="-2.286" y2="0.254" layer="51"/>
<rectangle x1="2.286" y1="-0.254" x2="2.794" y2="0.254" layer="51"/>
</package>
<package name="1X03/90">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<wire x1="-3.81" y1="-1.905" x2="-1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-1.27" y1="0.635" x2="-3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="-3.81" y1="0.635" x2="-3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="-2.54" y1="6.985" x2="-2.54" y2="1.27" width="0.762" layer="21"/>
<wire x1="-1.27" y1="-1.905" x2="1.27" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="1.27" y1="0.635" x2="-1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="0" y1="6.985" x2="0" y2="1.27" width="0.762" layer="21"/>
<wire x1="1.27" y1="-1.905" x2="3.81" y2="-1.905" width="0.1524" layer="21"/>
<wire x1="3.81" y1="-1.905" x2="3.81" y2="0.635" width="0.1524" layer="21"/>
<wire x1="3.81" y1="0.635" x2="1.27" y2="0.635" width="0.1524" layer="21"/>
<wire x1="2.54" y1="6.985" x2="2.54" y2="1.27" width="0.762" layer="21"/>
<pad name="1" x="-2.54" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="2" x="0" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<pad name="3" x="2.54" y="-3.81" drill="1.016" shape="long" rot="R90"/>
<text x="-4.445" y="-3.81" size="1.27" layer="25" ratio="10" rot="R90">&gt;NAME</text>
<text x="5.715" y="-3.81" size="1.27" layer="27" rot="R90">&gt;VALUE</text>
<rectangle x1="-2.921" y1="0.635" x2="-2.159" y2="1.143" layer="21"/>
<rectangle x1="-0.381" y1="0.635" x2="0.381" y2="1.143" layer="21"/>
<rectangle x1="2.159" y1="0.635" x2="2.921" y2="1.143" layer="21"/>
<rectangle x1="-2.921" y1="-2.921" x2="-2.159" y2="-1.905" layer="21"/>
<rectangle x1="-0.381" y1="-2.921" x2="0.381" y2="-1.905" layer="21"/>
<rectangle x1="2.159" y1="-2.921" x2="2.921" y2="-1.905" layer="21"/>
</package>
</packages>
<symbols>
<symbol name="PINHD3">
<wire x1="-6.35" y1="-5.08" x2="1.27" y2="-5.08" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-5.08" x2="1.27" y2="5.08" width="0.4064" layer="94"/>
<wire x1="1.27" y1="5.08" x2="-6.35" y2="5.08" width="0.4064" layer="94"/>
<wire x1="-6.35" y1="5.08" x2="-6.35" y2="-5.08" width="0.4064" layer="94"/>
<text x="-6.35" y="5.715" size="1.778" layer="95">&gt;NAME</text>
<text x="-6.35" y="-7.62" size="1.778" layer="96">&gt;VALUE</text>
<pin name="1" x="-2.54" y="2.54" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="2" x="-2.54" y="0" visible="pad" length="short" direction="pas" function="dot"/>
<pin name="3" x="-2.54" y="-2.54" visible="pad" length="short" direction="pas" function="dot"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="PINHD-1X3" prefix="JP" uservalue="yes">
<description>&lt;b&gt;PIN HEADER&lt;/b&gt;</description>
<gates>
<gate name="A" symbol="PINHD3" x="0" y="0"/>
</gates>
<devices>
<device name="" package="1X03">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="/90" package="1X03/90">
<connects>
<connect gate="A" pin="1" pad="1"/>
<connect gate="A" pin="2" pad="2"/>
<connect gate="A" pin="3" pad="3"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="cmc-rca-sockets">
<packages>
<package name="CMC_RCA_816">
<circle x="0" y="0" radius="4.5" width="0.1" layer="21"/>
<pad name="SIGNAL" x="0" y="0" drill="3.2" diameter="4.5"/>
<circle x="0" y="0" radius="5.25" width="2.5" layer="16"/>
<wire x1="0.5" y1="6" x2="5.5" y2="1" width="0.127" layer="21" curve="-90"/>
<wire x1="5.5" y1="1" x2="5.5" y2="-1" width="0.127" layer="21"/>
<wire x1="-5.5" y1="-1" x2="-5.5" y2="1" width="0.127" layer="21"/>
<wire x1="-5.5" y1="1" x2="-0.5" y2="6" width="0.127" layer="21" curve="-90"/>
<wire x1="-0.5" y1="6" x2="0.5" y2="6" width="0.127" layer="21"/>
<wire x1="-5.5" y1="-1" x2="-0.5" y2="-6" width="0.127" layer="21" curve="90"/>
<wire x1="-0.5" y1="-6" x2="0.5" y2="-6" width="0.127" layer="21"/>
<wire x1="0.5" y1="-6" x2="5.5" y2="-1" width="0.127" layer="21" curve="90"/>
<circle x="0" y="0" radius="5.25" width="2.7" layer="30"/>
<smd name="GND" x="5.7" y="0" dx="1.27" dy="0.635" layer="16" rot="R90"/>
</package>
<package name="CMC_RCA_805">
<circle x="0" y="0" radius="7.75" width="0.2" layer="27"/>
<circle x="0" y="0" radius="6" width="0.1" layer="21"/>
<circle x="0" y="0" radius="4" width="0.1" layer="21"/>
<pad name="SIGNAL" x="0" y="0" drill="3"/>
<pad name="GND1" x="-5" y="0" drill="3.5"/>
<pad name="GND2" x="5" y="0" drill="3.5"/>
<text x="8.255" y="5.08" size="1.016" layer="25" font="vector" ratio="10" distance="49" rot="R135">&gt;NAME</text>
<text x="1.905" y="5.08" size="0.6096" layer="27" font="vector" ratio="10" rot="R180">&gt;VALUE</text>
</package>
</packages>
<symbols>
<symbol name="RCA">
<pin name="SIGNAL" x="-1.27" y="-6.35" visible="off" length="short" rot="R90"/>
<pin name="GND" x="1.27" y="-6.35" visible="off" length="short" rot="R90"/>
<polygon width="0.254" layer="95">
<vertex x="2.54" y="-1.27"/>
<vertex x="2.54" y="-3.81"/>
<vertex x="-2.54" y="-3.81"/>
<vertex x="-2.54" y="-1.27"/>
</polygon>
<polygon width="0.254" layer="94">
<vertex x="-1.905" y="-0.635"/>
<vertex x="1.905" y="-0.635"/>
<vertex x="1.905" y="-1.27"/>
<vertex x="-1.905" y="-1.27"/>
</polygon>
<polygon width="0.254" layer="95">
<vertex x="-1.27" y="3.175"/>
<vertex x="1.27" y="3.175"/>
<vertex x="1.27" y="-0.635"/>
<vertex x="-1.27" y="-0.635"/>
</polygon>
<wire x1="-1.27" y1="1.905" x2="1.27" y2="1.905" width="0.254" layer="94"/>
<text x="3.175" y="0" size="1.27" layer="95" rot="R90">&gt;NAME</text>
<circle x="-1.27" y="-3.175" radius="0.127" width="0.254" layer="94"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="CMC_RCA" prefix="RCA">
<description>RCA sockets</description>
<gates>
<gate name="G$1" symbol="RCA" x="0" y="0"/>
</gates>
<devices>
<device name="805" package="CMC_RCA_805">
<connects>
<connect gate="G$1" pin="GND" pad="GND1 GND2"/>
<connect gate="G$1" pin="SIGNAL" pad="SIGNAL"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
<device name="816" package="CMC_RCA_816">
<connects>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="SIGNAL" pad="SIGNAL"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="RCA1L" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA1R" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA2L" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA2R" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA3L" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA3R" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA4L" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA4R" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA5L" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA5R" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA6L" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCA6R" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="IN1" library="pinhead" deviceset="PINHD-1X3" device=""/>
<part name="IN2" library="pinhead" deviceset="PINHD-1X3" device=""/>
<part name="IN3" library="pinhead" deviceset="PINHD-1X3" device=""/>
<part name="IN4" library="pinhead" deviceset="PINHD-1X3" device=""/>
<part name="IN5" library="pinhead" deviceset="PINHD-1X3" device=""/>
<part name="IN6" library="pinhead" deviceset="PINHD-1X3" device=""/>
<part name="RCAOUTR" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="RCAOUTL" library="cmc-rca-sockets" deviceset="CMC_RCA" device="816"/>
<part name="OUT" library="pinhead" deviceset="PINHD-1X3" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="RCA1L" gate="G$1" x="12.7" y="22.86"/>
<instance part="RCA1R" gate="G$1" x="17.78" y="22.86"/>
<instance part="RCA2L" gate="G$1" x="25.4" y="22.86"/>
<instance part="RCA2R" gate="G$1" x="30.48" y="22.86"/>
<instance part="RCA3L" gate="G$1" x="38.1" y="22.86"/>
<instance part="RCA3R" gate="G$1" x="43.18" y="22.86"/>
<instance part="RCA4L" gate="G$1" x="50.8" y="22.86"/>
<instance part="RCA4R" gate="G$1" x="55.88" y="22.86"/>
<instance part="RCA5L" gate="G$1" x="63.5" y="22.86"/>
<instance part="RCA5R" gate="G$1" x="68.58" y="22.86"/>
<instance part="RCA6L" gate="G$1" x="76.2" y="22.86"/>
<instance part="RCA6R" gate="G$1" x="81.28" y="22.86"/>
<instance part="IN1" gate="A" x="13.97" y="5.08" rot="R270"/>
<instance part="IN2" gate="A" x="26.67" y="5.08" rot="R270"/>
<instance part="IN3" gate="A" x="39.37" y="5.08" rot="R270"/>
<instance part="IN4" gate="A" x="52.07" y="5.08" rot="R270"/>
<instance part="IN5" gate="A" x="64.77" y="5.08" rot="R270"/>
<instance part="IN6" gate="A" x="77.47" y="5.08" rot="R270"/>
<instance part="RCAOUTR" gate="G$1" x="99.06" y="22.86"/>
<instance part="RCAOUTL" gate="G$1" x="93.98" y="22.86"/>
<instance part="OUT" gate="A" x="95.25" y="5.08" rot="R270"/>
</instances>
<busses>
</busses>
<nets>
<net name="N$4" class="0">
<segment>
<pinref part="RCA2R" gate="G$1" pin="SIGNAL"/>
<pinref part="IN2" gate="A" pin="1"/>
<wire x1="29.21" y1="7.62" x2="29.21" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$6" class="0">
<segment>
<pinref part="RCA3R" gate="G$1" pin="SIGNAL"/>
<pinref part="IN3" gate="A" pin="1"/>
<wire x1="41.91" y1="7.62" x2="41.91" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$8" class="0">
<segment>
<pinref part="RCA4R" gate="G$1" pin="SIGNAL"/>
<pinref part="IN4" gate="A" pin="1"/>
<wire x1="54.61" y1="7.62" x2="54.61" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$10" class="0">
<segment>
<pinref part="RCA5R" gate="G$1" pin="SIGNAL"/>
<pinref part="IN5" gate="A" pin="1"/>
<wire x1="67.31" y1="7.62" x2="67.31" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$12" class="0">
<segment>
<pinref part="RCA6R" gate="G$1" pin="SIGNAL"/>
<pinref part="IN6" gate="A" pin="1"/>
<wire x1="80.01" y1="7.62" x2="80.01" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="RCA1L" gate="G$1" pin="SIGNAL"/>
<pinref part="IN1" gate="A" pin="3"/>
<wire x1="11.43" y1="7.62" x2="11.43" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$13" class="0">
<segment>
<pinref part="RCA1R" gate="G$1" pin="SIGNAL"/>
<pinref part="IN1" gate="A" pin="1"/>
<wire x1="16.51" y1="7.62" x2="16.51" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="RCA2L" gate="G$1" pin="SIGNAL"/>
<pinref part="IN2" gate="A" pin="3"/>
<wire x1="24.13" y1="16.51" x2="24.13" y2="7.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="RCA3L" gate="G$1" pin="SIGNAL"/>
<pinref part="IN3" gate="A" pin="3"/>
<wire x1="36.83" y1="16.51" x2="36.83" y2="7.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<pinref part="RCA4L" gate="G$1" pin="SIGNAL"/>
<pinref part="IN4" gate="A" pin="3"/>
<wire x1="49.53" y1="16.51" x2="49.53" y2="7.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<pinref part="RCA5L" gate="G$1" pin="SIGNAL"/>
<pinref part="IN5" gate="A" pin="3"/>
<wire x1="62.23" y1="16.51" x2="62.23" y2="7.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$9" class="0">
<segment>
<pinref part="RCA6L" gate="G$1" pin="SIGNAL"/>
<pinref part="IN6" gate="A" pin="3"/>
<wire x1="74.93" y1="16.51" x2="74.93" y2="7.62" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$11" class="0">
<segment>
<pinref part="RCAOUTR" gate="G$1" pin="SIGNAL"/>
<pinref part="OUT" gate="A" pin="1"/>
<wire x1="97.79" y1="7.62" x2="97.79" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$15" class="0">
<segment>
<pinref part="RCAOUTL" gate="G$1" pin="SIGNAL"/>
<pinref part="OUT" gate="A" pin="3"/>
<wire x1="92.71" y1="7.62" x2="92.71" y2="16.51" width="0.1524" layer="91"/>
</segment>
</net>
<net name="GNDOUT" class="0">
<segment>
<pinref part="OUT" gate="A" pin="2"/>
<pinref part="RCAOUTL" gate="G$1" pin="GND"/>
<wire x1="95.25" y1="7.62" x2="95.25" y2="13.97" width="0.1524" layer="91"/>
<pinref part="RCAOUTR" gate="G$1" pin="GND"/>
<wire x1="100.33" y1="16.51" x2="100.33" y2="13.97" width="0.1524" layer="91"/>
<wire x1="100.33" y1="13.97" x2="95.25" y2="13.97" width="0.1524" layer="91"/>
<wire x1="95.25" y1="13.97" x2="95.25" y2="16.51" width="0.1524" layer="91"/>
<junction x="95.25" y="13.97"/>
</segment>
</net>
<net name="GND2" class="0">
<segment>
<pinref part="RCA2L" gate="G$1" pin="GND"/>
<pinref part="IN2" gate="A" pin="2"/>
<wire x1="26.67" y1="7.62" x2="26.67" y2="15.24" width="0.1524" layer="91"/>
<pinref part="RCA2R" gate="G$1" pin="GND"/>
<wire x1="26.67" y1="15.24" x2="26.67" y2="16.51" width="0.1524" layer="91"/>
<wire x1="31.75" y1="16.51" x2="31.75" y2="15.24" width="0.1524" layer="91"/>
<wire x1="31.75" y1="15.24" x2="26.67" y2="15.24" width="0.1524" layer="91"/>
<junction x="26.67" y="15.24"/>
</segment>
</net>
<net name="GND3" class="0">
<segment>
<pinref part="RCA3L" gate="G$1" pin="GND"/>
<pinref part="IN3" gate="A" pin="2"/>
<wire x1="39.37" y1="7.62" x2="39.37" y2="15.24" width="0.1524" layer="91"/>
<pinref part="RCA3R" gate="G$1" pin="GND"/>
<wire x1="39.37" y1="15.24" x2="39.37" y2="16.51" width="0.1524" layer="91"/>
<wire x1="44.45" y1="16.51" x2="44.45" y2="15.24" width="0.1524" layer="91"/>
<wire x1="44.45" y1="15.24" x2="39.37" y2="15.24" width="0.1524" layer="91"/>
<junction x="39.37" y="15.24"/>
</segment>
</net>
<net name="GND4" class="0">
<segment>
<pinref part="RCA4L" gate="G$1" pin="GND"/>
<pinref part="IN4" gate="A" pin="2"/>
<wire x1="52.07" y1="7.62" x2="52.07" y2="15.24" width="0.1524" layer="91"/>
<pinref part="RCA4R" gate="G$1" pin="GND"/>
<wire x1="52.07" y1="15.24" x2="52.07" y2="16.51" width="0.1524" layer="91"/>
<wire x1="57.15" y1="16.51" x2="57.15" y2="15.24" width="0.1524" layer="91"/>
<wire x1="57.15" y1="15.24" x2="52.07" y2="15.24" width="0.1524" layer="91"/>
<junction x="52.07" y="15.24"/>
</segment>
</net>
<net name="GND5" class="0">
<segment>
<pinref part="RCA5L" gate="G$1" pin="GND"/>
<pinref part="IN5" gate="A" pin="2"/>
<wire x1="64.77" y1="7.62" x2="64.77" y2="15.24" width="0.1524" layer="91"/>
<pinref part="RCA5R" gate="G$1" pin="GND"/>
<wire x1="64.77" y1="15.24" x2="64.77" y2="16.51" width="0.1524" layer="91"/>
<wire x1="69.85" y1="16.51" x2="69.85" y2="15.24" width="0.1524" layer="91"/>
<wire x1="69.85" y1="15.24" x2="64.77" y2="15.24" width="0.1524" layer="91"/>
<junction x="64.77" y="15.24"/>
</segment>
</net>
<net name="GND1" class="0">
<segment>
<pinref part="IN1" gate="A" pin="2"/>
<pinref part="RCA1L" gate="G$1" pin="GND"/>
<wire x1="13.97" y1="7.62" x2="13.97" y2="15.24" width="0.1524" layer="91"/>
<pinref part="RCA1R" gate="G$1" pin="GND"/>
<wire x1="13.97" y1="15.24" x2="13.97" y2="16.51" width="0.1524" layer="91"/>
<wire x1="19.05" y1="16.51" x2="19.05" y2="15.24" width="0.1524" layer="91"/>
<wire x1="19.05" y1="15.24" x2="13.97" y2="15.24" width="0.1524" layer="91"/>
<junction x="13.97" y="15.24"/>
</segment>
</net>
<net name="GND6" class="0">
<segment>
<pinref part="RCA6R" gate="G$1" pin="GND"/>
<wire x1="82.55" y1="16.51" x2="82.55" y2="15.24" width="0.1524" layer="91"/>
<wire x1="82.55" y1="15.24" x2="77.47" y2="15.24" width="0.1524" layer="91"/>
<pinref part="RCA6L" gate="G$1" pin="GND"/>
<wire x1="77.47" y1="15.24" x2="77.47" y2="16.51" width="0.1524" layer="91"/>
<pinref part="IN6" gate="A" pin="2"/>
<wire x1="77.47" y1="15.24" x2="77.47" y2="7.62" width="0.1524" layer="91"/>
<junction x="77.47" y="15.24"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
