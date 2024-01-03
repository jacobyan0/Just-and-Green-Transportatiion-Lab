# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-08-10 01:21:44
"""
import arcpy

def Model1():  # Model1

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    result3_shp_2_ = "C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp"
    new_stops_2_ = "new stops"
    result3_shp = "C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp"

    # Process: Spatial Join (Spatial Join) (analysis)
    result4_shp = "C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result4.shp"
    arcpy.analysis.SpatialJoin(target_features=result3_shp_2_, join_features=new_stops_2_, out_feature_class=result4_shp, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="inner_scoo \"inner_scoo\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,inner_scoo,-1,-1;TARGET_FID \"TARGET_FID\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,TARGET_FID,-1,-1;inner_micr \"inner_micr\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,inner_micr,-1,-1;TARGET_F_1 \"TARGET_F_1\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,TARGET_F_1,-1,-1;Route \"Route\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,Route,-1,-1;total_trip \"total_trip\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,total_trip,-1,-1;Total_Acti \"Total_Acti\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,Total_Acti,-1,-1;W_C_TOTAL \"W_C_TOTAL\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,W_C_TOTAL,-1,-1;BIKE_TOTAL \"BIKE_TOTAL\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BIKE_TOTAL,-1,-1;index \"index\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,index,-1,-1;lat \"lat\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lat,-1,-1;lon \"lon\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lon,-1,-1;lat_1 \"lat_1\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lat_1,-1,-1;lon_1 \"lon_1\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lon_1,-1,-1;fmlm_score \"fmlm_score\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,fmlm_score,-1,-1;D3BMM4 \"D3BMM4\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D3BMM4,-1,-1;D3BPO4 \"D3BPO4\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D3BPO4,-1,-1;D5AR \"D5AR\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D5AR,-1,-1;D5BR \"D5BR\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D5BR,-1,-1;osm \"osm\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,osm,-1,-1;sidewalk \"sidewalk\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,sidewalk,-1,-1;sidewalk_o \"sidewalk_o\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,sidewalk_o,-1,-1;bike \"bike\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,bike,-1,-1;bike_osm \"bike_osm\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,bike_osm,-1,-1;HISPANIC \"HISPANIC\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,HISPANIC,-1,-1;TOTALPOP \"TOTALPOP\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,TOTALPOP,-1,-1;HOUSEHOLDS \"HOUSEHOLDS\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,HOUSEHOLDS,-1,-1;VEHICLE_0 \"VEHICLE_0\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,VEHICLE_0,-1,-1;BLACK \"BLACK\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BLACK,-1,-1;RENTER \"RENTER\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,RENTER,-1,-1;AGE_65_UP \"AGE_65_UP\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,AGE_65_UP,-1,-1;DIS_2064 \"DIS_2064\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,DIS_2064,-1,-1;S_NOTATALL \"S_NOTATALL\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,S_NOTATALL,-1,-1;BELOW_POV \"BELOW_POV\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BELOW_POV,-1,-1;HISPANIC_ \"HISPANIC%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,HISPANIC%,-1,-1;VEHICLE_0_ \"VEHICLE_0%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,VEHICLE_0%,-1,-1;AGE_65_UP_ \"AGE_65_UP%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,AGE_65_UP%,-1,-1;DIS_2064_ \"DIS_2064%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,DIS_2064%,-1,-1;S_NOTATA_1 \"S_NOTATA_1\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,S_NOTATA_1,-1,-1;BELOW_POV_ \"BELOW_POV%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BELOW_POV%,-1,-1;BLACK_ \"BLACK%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BLACK%,-1,-1;RENT_ \"RENT%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,RENT%,-1,-1;inner_sc_1 \"inner_scoo\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,inner_scoo,-1,-1;TARGET_F_2 \"TARGET_FID\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,TARGET_FID,-1,-1;inner_mi_1 \"inner_micr\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,inner_micr,-1,-1;TARGET_F_3 \"TARGET_F_1\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,TARGET_F_1,-1,-1;Route_1 \"Route\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,Route,-1,-1;total_tr_1 \"total_trip\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,total_trip,-1,-1;Total_Ac_1 \"Total_Acti\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,Total_Acti,-1,-1;W_C_TOTA_1 \"W_C_TOTAL\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,W_C_TOTAL,-1,-1;BIKE_TOT_1 \"BIKE_TOTAL\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BIKE_TOTAL,-1,-1;index_1 \"index\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,index,-1,-1;lat_12 \"lat\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lat,-1,-1;lon_12 \"lon\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lon,-1,-1;lat_12_13 \"lat_1\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lat_1,-1,-1;lon_12_13 \"lon_1\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,lon_1,-1,-1;fmlm_sco_1 \"fmlm_score\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,fmlm_score,-1,-1;D3BMM4_1 \"D3BMM4\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D3BMM4,-1,-1;D3BPO4_1 \"D3BPO4\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D3BPO4,-1,-1;D5AR_1 \"D5AR\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D5AR,-1,-1;D5BR_1 \"D5BR\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,D5BR,-1,-1;osm_1 \"osm\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,osm,-1,-1;sidewalk_1 \"sidewalk\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,sidewalk,-1,-1;sidewalk_2 \"sidewalk_o\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,sidewalk_o,-1,-1;bike_1 \"bike\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,bike,-1,-1;bike_osm_1 \"bike_osm\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,bike_osm,-1,-1;HISPANIC_1 \"HISPANIC\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,HISPANIC,-1,-1;TOTALPOP_1 \"TOTALPOP\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,TOTALPOP,-1,-1;HOUSEHOL_1 \"HOUSEHOLDS\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,HOUSEHOLDS,-1,-1;VEHICLE_01 \"VEHICLE_0\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,VEHICLE_0,-1,-1;BLACK_1 \"BLACK\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BLACK,-1,-1;RENTER_1 \"RENTER\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,RENTER,-1,-1;AGE_65_U_1 \"AGE_65_UP\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,AGE_65_UP,-1,-1;DIS_2_2065 \"DIS_2064\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,DIS_2064,-1,-1;S_NOTATA_2 \"S_NOTATALL\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,S_NOTATALL,-1,-1;BELOW_PO_1 \"BELOW_POV\" true true false 18 Double 0 18,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BELOW_POV,-1,-1;HISPANIC1 \"HISPANIC%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,HISPANIC%,-1,-1;VEHICLE_02 \"VEHICLE_0%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,VEHICLE_0%,-1,-1;AGE_65_UP1 \"AGE_65_UP%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,AGE_65_UP%,-1,-1;DIS_20641 \"DIS_2064%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,DIS_2064%,-1,-1;S_NOTATA_3 \"S_NOTATA_1\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,S_NOTATA_1,-1,-1;BELOW_POV1 \"BELOW_POV%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BELOW_POV%,-1,-1;BLACK1 \"BLACK%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,BLACK%,-1,-1;RENT1 \"RENT%\" true true false 24 Double 15 23,First,#,C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp,RENT%,-1,-1", match_option="INTERSECT", search_radius="", distance_field_name="")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\anranzheng\OneDrive - University of Florida\Documents\ArcGIS\Projects\MyProject2\MyProject2.gdb", workspace=r"C:\Users\anranzheng\OneDrive - University of Florida\Documents\ArcGIS\Projects\MyProject2\MyProject2.gdb"):
        Model1()
