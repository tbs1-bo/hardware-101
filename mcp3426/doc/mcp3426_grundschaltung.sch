<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="8.2.1">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
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
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
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
<library name="con-ml">
<description>&lt;b&gt;Harting  Connectors&lt;/b&gt;&lt;p&gt;
Low profile connectors, straight&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="ML40">
<description>&lt;b&gt;HARTING&lt;/b&gt;</description>
<wire x1="-27.94" y1="3.175" x2="27.94" y2="3.175" width="0.127" layer="21"/>
<wire x1="27.94" y1="-3.175" x2="27.94" y2="3.175" width="0.127" layer="21"/>
<wire x1="-27.94" y1="3.175" x2="-27.94" y2="-3.175" width="0.127" layer="21"/>
<wire x1="-29.21" y1="4.445" x2="-27.94" y2="4.445" width="0.127" layer="21"/>
<wire x1="29.21" y1="-4.445" x2="24.511" y2="-4.445" width="0.127" layer="21"/>
<wire x1="29.21" y1="-4.445" x2="29.21" y2="4.445" width="0.127" layer="21"/>
<wire x1="-29.21" y1="4.445" x2="-29.21" y2="-4.445" width="0.127" layer="21"/>
<wire x1="27.94" y1="-3.175" x2="23.622" y2="-3.175" width="0.127" layer="21"/>
<wire x1="2.032" y1="-2.413" x2="-2.032" y2="-2.413" width="0.127" layer="21"/>
<wire x1="-2.032" y1="-3.175" x2="-2.032" y2="-2.413" width="0.127" layer="21"/>
<wire x1="-2.032" y1="-3.175" x2="-19.558" y2="-3.175" width="0.127" layer="21"/>
<wire x1="2.032" y1="-2.413" x2="2.032" y2="-3.175" width="0.127" layer="21"/>
<wire x1="2.032" y1="-3.175" x2="2.032" y2="-3.429" width="0.127" layer="21"/>
<wire x1="27.94" y1="4.445" x2="27.94" y2="4.699" width="0.127" layer="21"/>
<wire x1="27.94" y1="4.699" x2="26.67" y2="4.699" width="0.127" layer="21"/>
<wire x1="26.67" y1="4.445" x2="26.67" y2="4.699" width="0.127" layer="21"/>
<wire x1="27.94" y1="4.445" x2="29.21" y2="4.445" width="0.127" layer="21"/>
<wire x1="0.635" y1="4.699" x2="-0.635" y2="4.699" width="0.127" layer="21"/>
<wire x1="0.635" y1="4.699" x2="0.635" y2="4.445" width="0.127" layer="21"/>
<wire x1="0.635" y1="4.445" x2="26.67" y2="4.445" width="0.127" layer="21"/>
<wire x1="-0.635" y1="4.699" x2="-0.635" y2="4.445" width="0.127" layer="21"/>
<wire x1="-26.67" y1="4.699" x2="-27.94" y2="4.699" width="0.127" layer="21"/>
<wire x1="-27.94" y1="4.699" x2="-27.94" y2="4.445" width="0.127" layer="21"/>
<wire x1="-26.67" y1="4.699" x2="-26.67" y2="4.445" width="0.127" layer="21"/>
<wire x1="-26.67" y1="4.445" x2="-0.635" y2="4.445" width="0.127" layer="21"/>
<wire x1="21.209" y1="-4.445" x2="2.032" y2="-4.445" width="0.127" layer="21"/>
<wire x1="2.032" y1="-4.445" x2="-2.032" y2="-4.445" width="0.127" layer="21"/>
<wire x1="22.098" y1="-3.175" x2="22.098" y2="-3.429" width="0.127" layer="21"/>
<wire x1="22.098" y1="-3.175" x2="2.032" y2="-3.175" width="0.127" layer="21"/>
<wire x1="23.622" y1="-3.175" x2="23.622" y2="-3.429" width="0.127" layer="21"/>
<wire x1="23.622" y1="-3.175" x2="22.098" y2="-3.175" width="0.127" layer="21"/>
<wire x1="21.209" y1="-4.445" x2="21.59" y2="-3.937" width="0.127" layer="21"/>
<wire x1="24.13" y1="-3.937" x2="24.511" y2="-4.445" width="0.127" layer="21"/>
<wire x1="24.13" y1="-3.937" x2="23.622" y2="-3.937" width="0.127" layer="21"/>
<wire x1="22.098" y1="-3.429" x2="2.032" y2="-3.429" width="0.0508" layer="21"/>
<wire x1="2.032" y1="-3.429" x2="2.032" y2="-4.445" width="0.127" layer="21"/>
<wire x1="23.622" y1="-3.429" x2="28.194" y2="-3.429" width="0.0508" layer="21"/>
<wire x1="28.194" y1="-3.429" x2="28.194" y2="3.429" width="0.0508" layer="21"/>
<wire x1="28.194" y1="3.429" x2="-28.194" y2="3.429" width="0.0508" layer="21"/>
<wire x1="-28.194" y1="3.429" x2="-28.194" y2="-3.429" width="0.0508" layer="21"/>
<wire x1="-28.194" y1="-3.429" x2="-21.082" y2="-3.429" width="0.0508" layer="21"/>
<wire x1="-2.032" y1="-3.175" x2="-2.032" y2="-3.429" width="0.127" layer="21"/>
<wire x1="-2.032" y1="-3.429" x2="-2.032" y2="-4.445" width="0.127" layer="21"/>
<wire x1="22.098" y1="-3.429" x2="22.098" y2="-3.937" width="0.127" layer="21"/>
<wire x1="22.098" y1="-3.937" x2="21.59" y2="-3.937" width="0.127" layer="21"/>
<wire x1="23.622" y1="-3.429" x2="23.622" y2="-3.937" width="0.127" layer="21"/>
<wire x1="23.622" y1="-3.937" x2="22.098" y2="-3.937" width="0.127" layer="21"/>
<wire x1="-29.21" y1="-4.445" x2="-24.892" y2="-4.445" width="0.127" layer="21"/>
<wire x1="-24.892" y1="-4.318" x2="-24.892" y2="-4.445" width="0.127" layer="21"/>
<wire x1="-24.892" y1="-4.318" x2="-23.368" y2="-4.318" width="0.127" layer="21"/>
<wire x1="-23.368" y1="-4.445" x2="-23.368" y2="-4.318" width="0.127" layer="21"/>
<wire x1="-23.368" y1="-4.445" x2="-21.971" y2="-4.445" width="0.127" layer="21"/>
<wire x1="-21.082" y1="-3.429" x2="-21.082" y2="-3.937" width="0.127" layer="21"/>
<wire x1="-19.558" y1="-3.429" x2="-19.558" y2="-3.937" width="0.127" layer="21"/>
<wire x1="-19.558" y1="-3.429" x2="-2.032" y2="-3.429" width="0.0508" layer="21"/>
<wire x1="-21.082" y1="-3.175" x2="-21.082" y2="-3.429" width="0.127" layer="21"/>
<wire x1="-21.082" y1="-3.175" x2="-27.94" y2="-3.175" width="0.127" layer="21"/>
<wire x1="-19.558" y1="-3.175" x2="-19.558" y2="-3.429" width="0.127" layer="21"/>
<wire x1="-19.558" y1="-3.175" x2="-21.082" y2="-3.175" width="0.127" layer="21"/>
<wire x1="-19.558" y1="-3.937" x2="-21.082" y2="-3.937" width="0.127" layer="21"/>
<wire x1="-21.082" y1="-3.937" x2="-21.59" y2="-3.937" width="0.127" layer="21"/>
<wire x1="-21.971" y1="-4.445" x2="-21.59" y2="-3.937" width="0.127" layer="21"/>
<wire x1="-19.05" y1="-3.937" x2="-18.669" y2="-4.445" width="0.127" layer="21"/>
<wire x1="-18.669" y1="-4.445" x2="-2.032" y2="-4.445" width="0.127" layer="21"/>
<wire x1="-19.05" y1="-3.937" x2="-19.558" y2="-3.937" width="0.127" layer="21"/>
<pad name="1" x="-24.13" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="2" x="-24.13" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="3" x="-21.59" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="4" x="-21.59" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="5" x="-19.05" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="6" x="-19.05" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="7" x="-16.51" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="8" x="-16.51" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="9" x="-13.97" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="10" x="-13.97" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="11" x="-11.43" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="12" x="-11.43" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="13" x="-8.89" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="14" x="-8.89" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="15" x="-6.35" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="16" x="-6.35" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="17" x="-3.81" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="18" x="-3.81" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="19" x="-1.27" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="20" x="-1.27" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="21" x="1.27" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="22" x="1.27" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="23" x="3.81" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="24" x="3.81" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="25" x="6.35" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="26" x="6.35" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="27" x="8.89" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="28" x="8.89" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="30" x="11.43" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="29" x="11.43" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="31" x="13.97" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="32" x="13.97" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="34" x="16.51" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="33" x="16.51" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="35" x="19.05" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="36" x="19.05" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="38" x="21.59" y="1.27" drill="0.9144" shape="octagon"/>
<pad name="37" x="21.59" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="39" x="24.13" y="-1.27" drill="0.9144" shape="octagon"/>
<pad name="40" x="24.13" y="1.27" drill="0.9144" shape="octagon"/>
<text x="-29.21" y="5.08" size="1.778" layer="25" ratio="10">&gt;NAME</text>
<text x="-15.24" y="5.08" size="1.778" layer="27" ratio="10">&gt;VALUE</text>
<text x="-26.67" y="-1.905" size="1.27" layer="21" ratio="10">1</text>
<text x="-26.67" y="0.635" size="1.27" layer="21" ratio="10">2</text>
<text x="-1.016" y="-4.064" size="1.27" layer="21" ratio="10">40</text>
<rectangle x1="6.096" y1="1.016" x2="6.604" y2="1.524" layer="51"/>
<rectangle x1="6.096" y1="-1.524" x2="6.604" y2="-1.016" layer="51"/>
<rectangle x1="3.556" y1="1.016" x2="4.064" y2="1.524" layer="51"/>
<rectangle x1="-6.604" y1="1.016" x2="-6.096" y2="1.524" layer="51"/>
<rectangle x1="-6.604" y1="-1.524" x2="-6.096" y2="-1.016" layer="51"/>
<rectangle x1="3.556" y1="-1.524" x2="4.064" y2="-1.016" layer="51"/>
<rectangle x1="-21.844" y1="1.016" x2="-21.336" y2="1.524" layer="51"/>
<rectangle x1="-24.384" y1="1.016" x2="-23.876" y2="1.524" layer="51"/>
<rectangle x1="-19.304" y1="1.016" x2="-18.796" y2="1.524" layer="51"/>
<rectangle x1="-9.144" y1="1.016" x2="-8.636" y2="1.524" layer="51"/>
<rectangle x1="-11.684" y1="1.016" x2="-11.176" y2="1.524" layer="51"/>
<rectangle x1="-21.844" y1="-1.524" x2="-21.336" y2="-1.016" layer="51"/>
<rectangle x1="-24.384" y1="-1.524" x2="-23.876" y2="-1.016" layer="51"/>
<rectangle x1="-19.304" y1="-1.524" x2="-18.796" y2="-1.016" layer="51"/>
<rectangle x1="-9.144" y1="-1.524" x2="-8.636" y2="-1.016" layer="51"/>
<rectangle x1="-11.684" y1="-1.524" x2="-11.176" y2="-1.016" layer="51"/>
<rectangle x1="-16.764" y1="-1.524" x2="-16.256" y2="-1.016" layer="51"/>
<rectangle x1="-16.764" y1="1.016" x2="-16.256" y2="1.524" layer="51"/>
<rectangle x1="1.016" y1="1.016" x2="1.524" y2="1.524" layer="51"/>
<rectangle x1="1.016" y1="-1.524" x2="1.524" y2="-1.016" layer="51"/>
<rectangle x1="-14.224" y1="1.016" x2="-13.716" y2="1.524" layer="51"/>
<rectangle x1="-14.224" y1="-1.524" x2="-13.716" y2="-1.016" layer="51"/>
<rectangle x1="-4.064" y1="1.016" x2="-3.556" y2="1.524" layer="51"/>
<rectangle x1="-1.524" y1="1.016" x2="-1.016" y2="1.524" layer="51"/>
<rectangle x1="-4.064" y1="-1.524" x2="-3.556" y2="-1.016" layer="51"/>
<rectangle x1="-1.524" y1="-1.524" x2="-1.016" y2="-1.016" layer="51"/>
<rectangle x1="8.636" y1="1.016" x2="9.144" y2="1.524" layer="51"/>
<rectangle x1="11.176" y1="1.016" x2="11.684" y2="1.524" layer="51"/>
<rectangle x1="21.336" y1="1.016" x2="21.844" y2="1.524" layer="51"/>
<rectangle x1="23.876" y1="1.016" x2="24.384" y2="1.524" layer="51"/>
<rectangle x1="8.636" y1="-1.524" x2="9.144" y2="-1.016" layer="51"/>
<rectangle x1="11.176" y1="-1.524" x2="11.684" y2="-1.016" layer="51"/>
<rectangle x1="21.336" y1="-1.524" x2="21.844" y2="-1.016" layer="51"/>
<rectangle x1="23.876" y1="-1.524" x2="24.384" y2="-1.016" layer="51"/>
<rectangle x1="13.716" y1="1.016" x2="14.224" y2="1.524" layer="51"/>
<rectangle x1="16.256" y1="1.016" x2="16.764" y2="1.524" layer="51"/>
<rectangle x1="18.796" y1="1.016" x2="19.304" y2="1.524" layer="51"/>
<rectangle x1="13.716" y1="-1.524" x2="14.224" y2="-1.016" layer="51"/>
<rectangle x1="16.256" y1="-1.524" x2="16.764" y2="-1.016" layer="51"/>
<rectangle x1="18.796" y1="-1.524" x2="19.304" y2="-1.016" layer="51"/>
</package>
</packages>
<symbols>
<symbol name="40P">
<wire x1="3.81" y1="-27.94" x2="-3.81" y2="-27.94" width="0.4064" layer="94"/>
<wire x1="-3.81" y1="25.4" x2="-3.81" y2="-27.94" width="0.4064" layer="94"/>
<wire x1="-3.81" y1="25.4" x2="3.81" y2="25.4" width="0.4064" layer="94"/>
<wire x1="3.81" y1="-27.94" x2="3.81" y2="25.4" width="0.4064" layer="94"/>
<wire x1="1.27" y1="-15.24" x2="2.54" y2="-15.24" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-17.78" x2="2.54" y2="-17.78" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-20.32" x2="2.54" y2="-20.32" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-22.86" x2="2.54" y2="-22.86" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-25.4" x2="2.54" y2="-25.4" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-15.24" x2="-1.27" y2="-15.24" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-17.78" x2="-1.27" y2="-17.78" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-20.32" x2="-1.27" y2="-20.32" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-22.86" x2="-1.27" y2="-22.86" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-25.4" x2="-1.27" y2="-25.4" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-12.7" x2="2.54" y2="-12.7" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-10.16" x2="2.54" y2="-10.16" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-7.62" x2="2.54" y2="-7.62" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-5.08" x2="2.54" y2="-5.08" width="0.6096" layer="94"/>
<wire x1="1.27" y1="-2.54" x2="2.54" y2="-2.54" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-12.7" x2="-1.27" y2="-12.7" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-10.16" x2="-1.27" y2="-10.16" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-7.62" x2="-1.27" y2="-7.62" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-5.08" x2="-1.27" y2="-5.08" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="-2.54" x2="-1.27" y2="-2.54" width="0.6096" layer="94"/>
<wire x1="1.27" y1="0" x2="2.54" y2="0" width="0.6096" layer="94"/>
<wire x1="1.27" y1="2.54" x2="2.54" y2="2.54" width="0.6096" layer="94"/>
<wire x1="1.27" y1="5.08" x2="2.54" y2="5.08" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="0" x2="-1.27" y2="0" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="2.54" x2="-1.27" y2="2.54" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="5.08" x2="-1.27" y2="5.08" width="0.6096" layer="94"/>
<wire x1="1.27" y1="7.62" x2="2.54" y2="7.62" width="0.6096" layer="94"/>
<wire x1="1.27" y1="10.16" x2="2.54" y2="10.16" width="0.6096" layer="94"/>
<wire x1="1.27" y1="12.7" x2="2.54" y2="12.7" width="0.6096" layer="94"/>
<wire x1="1.27" y1="15.24" x2="2.54" y2="15.24" width="0.6096" layer="94"/>
<wire x1="1.27" y1="17.78" x2="2.54" y2="17.78" width="0.6096" layer="94"/>
<wire x1="1.27" y1="20.32" x2="2.54" y2="20.32" width="0.6096" layer="94"/>
<wire x1="1.27" y1="22.86" x2="2.54" y2="22.86" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="7.62" x2="-1.27" y2="7.62" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="10.16" x2="-1.27" y2="10.16" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="12.7" x2="-1.27" y2="12.7" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="15.24" x2="-1.27" y2="15.24" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="17.78" x2="-1.27" y2="17.78" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="20.32" x2="-1.27" y2="20.32" width="0.6096" layer="94"/>
<wire x1="-2.54" y1="22.86" x2="-1.27" y2="22.86" width="0.6096" layer="94"/>
<text x="-3.81" y="-30.48" size="1.778" layer="96">&gt;VALUE</text>
<text x="-3.81" y="26.289" size="1.778" layer="95">&gt;NAME</text>
<pin name="1" x="7.62" y="-25.4" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="3" x="7.62" y="-22.86" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="5" x="7.62" y="-20.32" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="7" x="7.62" y="-17.78" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="9" x="7.62" y="-15.24" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="11" x="7.62" y="-12.7" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="13" x="7.62" y="-10.16" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="15" x="7.62" y="-7.62" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="17" x="7.62" y="-5.08" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="19" x="7.62" y="-2.54" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="21" x="7.62" y="0" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="23" x="7.62" y="2.54" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="25" x="7.62" y="5.08" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="27" x="7.62" y="7.62" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="29" x="7.62" y="10.16" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="31" x="7.62" y="12.7" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="33" x="7.62" y="15.24" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="35" x="7.62" y="17.78" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="37" x="7.62" y="20.32" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="39" x="7.62" y="22.86" visible="pad" length="middle" direction="pas" rot="R180"/>
<pin name="2" x="-7.62" y="-25.4" visible="pad" length="middle" direction="pas"/>
<pin name="4" x="-7.62" y="-22.86" visible="pad" length="middle" direction="pas"/>
<pin name="6" x="-7.62" y="-20.32" visible="pad" length="middle" direction="pas"/>
<pin name="8" x="-7.62" y="-17.78" visible="pad" length="middle" direction="pas"/>
<pin name="10" x="-7.62" y="-15.24" visible="pad" length="middle" direction="pas"/>
<pin name="12" x="-7.62" y="-12.7" visible="pad" length="middle" direction="pas"/>
<pin name="14" x="-7.62" y="-10.16" visible="pad" length="middle" direction="pas"/>
<pin name="16" x="-7.62" y="-7.62" visible="pad" length="middle" direction="pas"/>
<pin name="18" x="-7.62" y="-5.08" visible="pad" length="middle" direction="pas"/>
<pin name="20" x="-7.62" y="-2.54" visible="pad" length="middle" direction="pas"/>
<pin name="22" x="-7.62" y="0" visible="pad" length="middle" direction="pas"/>
<pin name="24" x="-7.62" y="2.54" visible="pad" length="middle" direction="pas"/>
<pin name="26" x="-7.62" y="5.08" visible="pad" length="middle" direction="pas"/>
<pin name="28" x="-7.62" y="7.62" visible="pad" length="middle" direction="pas"/>
<pin name="30" x="-7.62" y="10.16" visible="pad" length="middle" direction="pas"/>
<pin name="32" x="-7.62" y="12.7" visible="pad" length="middle" direction="pas"/>
<pin name="34" x="-7.62" y="15.24" visible="pad" length="middle" direction="pas"/>
<pin name="36" x="-7.62" y="17.78" visible="pad" length="middle" direction="pas"/>
<pin name="38" x="-7.62" y="20.32" visible="pad" length="middle" direction="pas"/>
<pin name="40" x="-7.62" y="22.86" visible="pad" length="middle" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="ML40" prefix="SV" uservalue="yes">
<description>&lt;b&gt;HARTING&lt;/b&gt;</description>
<gates>
<gate name="1" symbol="40P" x="0" y="0"/>
</gates>
<devices>
<device name="" package="ML40">
<connects>
<connect gate="1" pin="1" pad="1"/>
<connect gate="1" pin="10" pad="10"/>
<connect gate="1" pin="11" pad="11"/>
<connect gate="1" pin="12" pad="12"/>
<connect gate="1" pin="13" pad="13"/>
<connect gate="1" pin="14" pad="14"/>
<connect gate="1" pin="15" pad="15"/>
<connect gate="1" pin="16" pad="16"/>
<connect gate="1" pin="17" pad="17"/>
<connect gate="1" pin="18" pad="18"/>
<connect gate="1" pin="19" pad="19"/>
<connect gate="1" pin="2" pad="2"/>
<connect gate="1" pin="20" pad="20"/>
<connect gate="1" pin="21" pad="21"/>
<connect gate="1" pin="22" pad="22"/>
<connect gate="1" pin="23" pad="23"/>
<connect gate="1" pin="24" pad="24"/>
<connect gate="1" pin="25" pad="25"/>
<connect gate="1" pin="26" pad="26"/>
<connect gate="1" pin="27" pad="27"/>
<connect gate="1" pin="28" pad="28"/>
<connect gate="1" pin="29" pad="29"/>
<connect gate="1" pin="3" pad="3"/>
<connect gate="1" pin="30" pad="30"/>
<connect gate="1" pin="31" pad="31"/>
<connect gate="1" pin="32" pad="32"/>
<connect gate="1" pin="33" pad="33"/>
<connect gate="1" pin="34" pad="34"/>
<connect gate="1" pin="35" pad="35"/>
<connect gate="1" pin="36" pad="36"/>
<connect gate="1" pin="37" pad="37"/>
<connect gate="1" pin="38" pad="38"/>
<connect gate="1" pin="39" pad="39"/>
<connect gate="1" pin="4" pad="4"/>
<connect gate="1" pin="40" pad="40"/>
<connect gate="1" pin="5" pad="5"/>
<connect gate="1" pin="6" pad="6"/>
<connect gate="1" pin="7" pad="7"/>
<connect gate="1" pin="8" pad="8"/>
<connect gate="1" pin="9" pad="9"/>
</connects>
<technologies>
<technology name="">
<attribute name="MF" value="" constant="no"/>
<attribute name="MPN" value="" constant="no"/>
<attribute name="OC_FARNELL" value="unknown" constant="no"/>
<attribute name="OC_NEWARK" value="unknown" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="mcp3426">
<packages>
<package name="MSOP8_MC">
<smd name="1" x="-2.0447" y="0.975003125" dx="1.524" dy="0.4572" layer="1"/>
<smd name="2" x="-2.0447" y="0.32499375" dx="1.524" dy="0.4572" layer="1"/>
<smd name="3" x="-2.0447" y="-0.32499375" dx="1.524" dy="0.4572" layer="1"/>
<smd name="4" x="-2.0447" y="-0.975003125" dx="1.524" dy="0.4572" layer="1"/>
<smd name="5" x="2.0447" y="-0.975003125" dx="1.524" dy="0.4572" layer="1"/>
<smd name="6" x="2.0447" y="-0.32499375" dx="1.524" dy="0.4572" layer="1"/>
<smd name="7" x="2.0447" y="0.32499375" dx="1.524" dy="0.4572" layer="1"/>
<smd name="8" x="2.0447" y="0.975003125" dx="1.524" dy="0.4572" layer="1"/>
<wire x1="-1.4986" y1="0.762" x2="-1.4986" y2="1.1684" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="1.1684" x2="-2.4384" y2="1.1684" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="1.1684" x2="-2.4384" y2="0.762" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="0.762" x2="-1.4986" y2="0.762" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="0.127" x2="-1.4986" y2="0.5334" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="0.5334" x2="-2.4384" y2="0.5334" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="0.5334" x2="-2.4384" y2="0.127" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="0.127" x2="-1.4986" y2="0.127" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="-0.5334" x2="-1.4986" y2="-0.127" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="-0.127" x2="-2.4384" y2="-0.127" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="-0.127" x2="-2.4384" y2="-0.5334" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="-0.5334" x2="-1.4986" y2="-0.5334" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="-1.1684" x2="-1.4986" y2="-0.762" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="-0.762" x2="-2.4384" y2="-0.762" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="-0.762" x2="-2.4384" y2="-1.1684" width="0.1524" layer="25"/>
<wire x1="-2.4384" y1="-1.1684" x2="-1.4986" y2="-1.1684" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="-0.762" x2="1.4986" y2="-1.1684" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="-1.1684" x2="2.4384" y2="-1.1684" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="-1.1684" x2="2.4384" y2="-0.762" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="-0.762" x2="1.4986" y2="-0.762" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="-0.127" x2="1.4986" y2="-0.5334" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="-0.5334" x2="2.4384" y2="-0.5334" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="-0.5334" x2="2.4384" y2="-0.127" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="-0.127" x2="1.4986" y2="-0.127" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="0.5334" x2="1.4986" y2="0.127" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="0.127" x2="2.4384" y2="0.127" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="0.127" x2="2.4384" y2="0.5334" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="0.5334" x2="1.4986" y2="0.5334" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="1.1684" x2="1.4986" y2="0.762" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="0.762" x2="2.4384" y2="0.762" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="0.762" x2="2.4384" y2="1.1684" width="0.1524" layer="25"/>
<wire x1="2.4384" y1="1.1684" x2="1.4986" y2="1.1684" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="-1.4986" x2="1.4986" y2="-1.4986" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="-1.4986" x2="1.4986" y2="1.4986" width="0.1524" layer="25"/>
<wire x1="1.4986" y1="1.4986" x2="0.3048" y2="1.4986" width="0.1524" layer="25"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="25"/>
<wire x1="-0.3048" y1="1.4986" x2="-1.4986" y2="1.4986" width="0.1524" layer="25"/>
<wire x1="-1.4986" y1="1.4986" x2="-1.4986" y2="-1.4986" width="0.1524" layer="25"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0" layer="25" curve="-180"/>
<text x="-2.8702" y="1.2954" size="1.27" layer="25" ratio="6" rot="SR0">*</text>
<text x="-2.8702" y="-0.635" size="1.27" layer="25" ratio="6" rot="SR0">&gt;NAME</text>
<wire x1="-1.143" y1="-1.4986" x2="1.143" y2="-1.4986" width="0.1524" layer="51"/>
<wire x1="1.143" y1="1.4986" x2="0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="-0.3048" y1="1.4986" x2="-1.143" y2="1.4986" width="0.1524" layer="51"/>
<wire x1="0.3048" y1="1.4986" x2="-0.3048" y2="1.4986" width="0" layer="51" curve="-180"/>
<text x="-2.8702" y="1.2954" size="1.27" layer="51" ratio="6" rot="SR0">*</text>
<text x="-3.4544" y="-0.635" size="1.27" layer="27" ratio="6" rot="SR0">&gt;VALUE</text>
</package>
</packages>
<symbols>
<symbol name="MCP3422-XXXX_MS">
<pin name="CH1+" x="0" y="0" direction="in"/>
<pin name="CH1-" x="0" y="-2.54" direction="in"/>
<pin name="VDD" x="0" y="-5.08" direction="pwr"/>
<pin name="SDA" x="0" y="-7.62"/>
<pin name="CH2-" x="55.88" y="0" direction="in" rot="R180"/>
<pin name="CH2+" x="55.88" y="-2.54" direction="in" rot="R180"/>
<pin name="VSS" x="55.88" y="-5.08" direction="pwr" rot="R180"/>
<pin name="SCL" x="55.88" y="-7.62" direction="in" rot="R180"/>
<wire x1="7.112" y1="0" x2="6.0452" y2="0.508" width="0.1524" layer="94"/>
<wire x1="7.112" y1="0" x2="6.0452" y2="-0.508" width="0.1524" layer="94"/>
<wire x1="7.112" y1="-2.54" x2="6.0452" y2="-2.032" width="0.1524" layer="94"/>
<wire x1="7.112" y1="-2.54" x2="6.0452" y2="-3.048" width="0.1524" layer="94"/>
<wire x1="7.112" y1="-7.62" x2="6.0452" y2="-7.112" width="0.1524" layer="94"/>
<wire x1="7.112" y1="-7.62" x2="6.0452" y2="-8.128" width="0.1524" layer="94"/>
<wire x1="5.5372" y1="-7.112" x2="4.4958" y2="-7.62" width="0.1524" layer="94"/>
<wire x1="5.5372" y1="-8.128" x2="4.4958" y2="-7.62" width="0.1524" layer="94"/>
<wire x1="48.768" y1="0" x2="49.8348" y2="0.508" width="0.1524" layer="94"/>
<wire x1="48.768" y1="0" x2="49.8348" y2="-0.508" width="0.1524" layer="94"/>
<wire x1="48.768" y1="-2.54" x2="49.8348" y2="-2.032" width="0.1524" layer="94"/>
<wire x1="48.768" y1="-2.54" x2="49.8348" y2="-3.048" width="0.1524" layer="94"/>
<wire x1="48.768" y1="-7.62" x2="49.8348" y2="-7.112" width="0.1524" layer="94"/>
<wire x1="48.768" y1="-7.62" x2="49.8348" y2="-8.128" width="0.1524" layer="94"/>
<wire x1="7.62" y1="5.08" x2="7.62" y2="-12.7" width="0.1524" layer="94"/>
<wire x1="7.62" y1="-12.7" x2="48.26" y2="-12.7" width="0.1524" layer="94"/>
<wire x1="48.26" y1="-12.7" x2="48.26" y2="5.08" width="0.1524" layer="94"/>
<wire x1="48.26" y1="5.08" x2="7.62" y2="5.08" width="0.1524" layer="94"/>
<text x="23.2156" y="9.1186" size="2.0828" layer="95" ratio="6" rot="SR0">&gt;NAME</text>
<text x="22.2758" y="6.5786" size="2.0828" layer="96" ratio="6" rot="SR0">&gt;VALUE</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="MCP3422-XXXX_MS" prefix="MCP">
<description>analog digital converter MCP3426</description>
<gates>
<gate name="A" symbol="MCP3422-XXXX_MS" x="0" y="0"/>
</gates>
<devices>
<device name="" package="MSOP8_MC">
<connects>
<connect gate="A" pin="CH1+" pad="1"/>
<connect gate="A" pin="CH1-" pad="2"/>
<connect gate="A" pin="CH2+" pad="7"/>
<connect gate="A" pin="CH2-" pad="8"/>
<connect gate="A" pin="SCL" pad="5"/>
<connect gate="A" pin="SDA" pad="4"/>
<connect gate="A" pin="VDD" pad="3"/>
<connect gate="A" pin="VSS" pad="6"/>
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
<part name="RASPI" library="con-ml" deviceset="ML40" device=""/>
<part name="MCP3426" library="mcp3426" deviceset="MCP3422-XXXX_MS" device="" value=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="RASPI" gate="1" x="83.82" y="-27.94" rot="R180"/>
<instance part="MCP3426" gate="A" x="12.7" y="-17.78"/>
</instances>
<busses>
</busses>
<nets>
<net name="N$1" class="0">
<segment>
<pinref part="RASPI" gate="1" pin="3"/>
<wire x1="76.2" y1="-5.08" x2="10.16" y2="-5.08" width="0.1524" layer="91"/>
<wire x1="10.16" y1="-5.08" x2="10.16" y2="-25.4" width="0.1524" layer="91"/>
<pinref part="MCP3426" gate="A" pin="SDA"/>
<wire x1="10.16" y1="-25.4" x2="12.7" y2="-25.4" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="RASPI" gate="1" pin="6"/>
<wire x1="91.44" y1="-7.62" x2="93.98" y2="-7.62" width="0.1524" layer="91"/>
<wire x1="93.98" y1="-7.62" x2="93.98" y2="2.54" width="0.1524" layer="91"/>
<wire x1="93.98" y1="2.54" x2="71.12" y2="2.54" width="0.1524" layer="91"/>
<wire x1="71.12" y1="2.54" x2="71.12" y2="-22.86" width="0.1524" layer="91"/>
<pinref part="MCP3426" gate="A" pin="VSS"/>
<wire x1="71.12" y1="-22.86" x2="68.58" y2="-22.86" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<pinref part="RASPI" gate="1" pin="1"/>
<wire x1="76.2" y1="-2.54" x2="7.62" y2="-2.54" width="0.1524" layer="91"/>
<wire x1="7.62" y1="-2.54" x2="7.62" y2="-22.86" width="0.1524" layer="91"/>
<pinref part="MCP3426" gate="A" pin="VDD"/>
<wire x1="7.62" y1="-22.86" x2="12.7" y2="-22.86" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="RASPI" gate="1" pin="5"/>
<wire x1="76.2" y1="-7.62" x2="73.66" y2="-7.62" width="0.1524" layer="91"/>
<wire x1="73.66" y1="-7.62" x2="73.66" y2="-25.4" width="0.1524" layer="91"/>
<pinref part="MCP3426" gate="A" pin="SCL"/>
<wire x1="73.66" y1="-25.4" x2="68.58" y2="-25.4" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
