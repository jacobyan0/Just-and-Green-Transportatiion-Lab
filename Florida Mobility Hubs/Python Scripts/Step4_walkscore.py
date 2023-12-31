# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2023-08-10 00:55:32
"""
import arcpy
def #  NOT  IMPLEMENTED# Function Body not implemented

def Model6():  # Model6

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Conversion Tools.tbx")
    arcpy.ImportToolbox(r"c:\program files\arcgis\pro\Resources\ArcToolbox\toolboxes\Data Management Tools.tbx")
    result3_shp = "C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\result3.shp"
    Walkscore_xlsx = "C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Data\\process data\\access\\Walkscore.xlsx"

    for I_result3_index, Value in #  NOT  IMPLEMENTED(result3_shp, [["index", ""]], False):

        # Process: Excel To Table (Excel To Table) (conversion)
        Walkscore_ExcelToTable = "C:\\Users\\anranzheng\\OneDrive - University of Florida\\Documents\\ArcGIS\\Projects\\gnv mobility hub\\gnv mobility hub.gdb\\Walkscore_ExcelToTable"
        arcpy.conversion.ExcelToTable(Input_Excel_File=Walkscore_xlsx, Output_Table=Walkscore_ExcelToTable, Sheet="", field_names_row=1, cell_range="")

        # Process: XY Table To Point (XY Table To Point) (management)
        walkscore_shp = "C:\\Users\\anranzheng\\Dropbox (UFL)\\Mobility Hub\\Anran\\module builder\\process\\walkscore.shp"
        arcpy.management.XYTableToPoint(in_table=Walkscore_ExcelToTable, out_feature_class=walkscore_shp, x_field="stop_lon", y_field="stop_lat", z_field="", coordinate_system="GEOGCS[\"GCS_WGS_1984\",DATUM[\"D_WGS_1984\",SPHEROID[\"WGS_1984\",6378137.0,298.257223563]],PRIMEM[\"Greenwich\",0.0],UNIT[\"Degree\",0.0174532925199433]];-400 -400 1000000000;-100000 10000;-100000 10000;8.98315284119521E-09;0.001;0.001;IsHighPrecision")

        # Process: Intersect (Intersect) (analysis)
        Value = "628"
        result3_Value_ = fr"C:\Users\anranzheng\OneDrive - University of Florida\Documents\ArcGIS\Projects\gnv mobility hub\gnv mobility hub.gdb\result3_{Value}"
        arcpy.analysis.Intersect(in_features=[[I_result3_index, ""], [walkscore_shp, ""]], out_feature_class=result3_Value_, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

        # Process: Copy Features (Copy Features) (management)
        walkscore_Value_shp = fr"C:\Users\anranzheng\Dropbox (UFL)\Mobility Hub\Anran\module builder\process\walkscore\walkscore{Value}.shp"
        arcpy.management.CopyFeatures(in_features=result3_Value_, out_feature_class=walkscore_Value_shp, config_keyword="", spatial_grid_1=None, spatial_grid_2=None, spatial_grid_3=None)

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"C:\Users\anranzheng\OneDrive - University of Florida\Documents\ArcGIS\Projects\gnv mobility hub\gnv mobility hub.gdb", workspace=r"C:\Users\anranzheng\OneDrive - University of Florida\Documents\ArcGIS\Projects\gnv mobility hub\gnv mobility hub.gdb"):
        Model6()
