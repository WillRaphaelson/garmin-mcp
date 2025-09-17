"""
FastMCP Echo Server
"""

from fastmcp import FastMCP

# Create server
app = FastMCP("Echo Server")

"""
Activity Management functions for Garmin Connect MCP Server
"""
import datetime
from typing import Any, Dict, List, Optional, Union
from garminconnect import Garmin
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("GARMIN_EMAIL")
password = os.getenv("GARMIN_PASSWORD")
garmin_client = Garmin(email, password)
garmin_client.login()


    
@app.tool()
async def get_activities_by_date(start_date: str, end_date: str, activity_type: str = "") -> str:
    """Get activities data between specified dates, optionally filtered by activity type
    
    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        activity_type: Optional activity type filter (e.g., cycling, running, swimming)
    """
    try:
        activities = garmin_client.get_activities_by_date(start_date, end_date, activity_type)
        if not activities:
            return f"No activities found between {start_date} and {end_date}" + \
                    (f" for activity type '{activity_type}'" if activity_type else "")
        
        return activities
    except Exception as e:
        return f"Error retrieving activities by date: {str(e)}"

@app.tool()
async def get_activities_fordate(date: str) -> str:
    """Get activities for a specific date
    
    Args:
        date: Date in YYYY-MM-DD format
    """
    try:
        activities = garmin_client.get_activities_fordate(date)
        if not activities:
            return f"No activities found for {date}"
        
        return activities
    except Exception as e:
        return f"Error retrieving activities for date: {str(e)}"

@app.tool()
async def get_activity(activity_id: int) -> str:
    """Get basic activity information
    
    Args:
        activity_id: ID of the activity to retrieve
    """
    try:
        activity = garmin_client.get_activity(activity_id)
        if not activity:
            return f"No activity found with ID {activity_id}"
        
        return activity
    except Exception as e:
        return f"Error retrieving activity: {str(e)}"

@app.tool()
async def get_activity_splits(activity_id: int) -> str:
    """Get splits for an activity
    
    Args:
        activity_id: ID of the activity to retrieve splits for
    """
    try:
        splits = garmin_client.get_activity_splits(activity_id)
        if not splits:
            return f"No splits found for activity with ID {activity_id}"
        
        return splits
    except Exception as e:
        return f"Error retrieving activity splits: {str(e)}"

@app.tool()
async def get_activity_typed_splits(activity_id: int) -> str:
    """Get typed splits for an activity
    
    Args:
        activity_id: ID of the activity to retrieve typed splits for
    """
    try:
        typed_splits = garmin_client.get_activity_typed_splits(activity_id)
        if not typed_splits:
            return f"No typed splits found for activity with ID {activity_id}"
        
        return typed_splits
    except Exception as e:
        return f"Error retrieving activity typed splits: {str(e)}"

@app.tool()
async def get_activity_split_summaries(activity_id: int) -> str:
    """Get split summaries for an activity
    
    Args:
        activity_id: ID of the activity to retrieve split summaries for
    """
    try:
        split_summaries = garmin_client.get_activity_split_summaries(activity_id)
        if not split_summaries:
            return f"No split summaries found for activity with ID {activity_id}"
        
        return split_summaries
    except Exception as e:
        return f"Error retrieving activity split summaries: {str(e)}"

@app.tool()
async def get_activity_weather(activity_id: int) -> str:
    """Get weather data for an activity
    
    Args:
        activity_id: ID of the activity to retrieve weather data for
    """
    try:
        weather = garmin_client.get_activity_weather(activity_id)
        if not weather:
            return f"No weather data found for activity with ID {activity_id}"
        
        return weather
    except Exception as e:
        return f"Error retrieving activity weather data: {str(e)}"

@app.tool()
async def get_activity_hr_in_timezones(activity_id: int) -> str:
    """Get heart rate data in different time zones for an activity
    
    Args:
        activity_id: ID of the activity to retrieve heart rate time zone data for
    """
    try:
        hr_zones = garmin_client.get_activity_hr_in_timezones(activity_id)
        if not hr_zones:
            return f"No heart rate time zone data found for activity with ID {activity_id}"
        
        return hr_zones
    except Exception as e:
        return f"Error retrieving activity heart rate time zone data: {str(e)}"

@app.tool()
async def get_activity_gear(activity_id: int) -> str:
    """Get gear data used for an activity
    
    Args:
        activity_id: ID of the activity to retrieve gear data for
    """
    try:
        gear = garmin_client.get_activity_gear(activity_id)
        if not gear:
            return f"No gear data found for activity with ID {activity_id}"
        
        return gear
    except Exception as e:
        return f"Error retrieving activity gear data: {str(e)}"

@app.tool()
async def get_activity_exercise_sets(activity_id: int) -> str:
    """Get exercise sets for strength training activities
    
    Args:
        activity_id: ID of the activity to retrieve exercise sets for
    """
    try:
        exercise_sets = garmin_client.get_activity_exercise_sets(activity_id)
        if not exercise_sets:
            return f"No exercise sets found for activity with ID {activity_id}"
        
        return exercise_sets
    except Exception as e:
        return f"Error retrieving activity exercise sets: {str(e)}"
    

@app.tool()
async def get_recent_activities() -> str:
    """Get recent activities"""
    try:
        activities = garmin_client.get_activities()
        if not activities:
            return "No recent activities found"
        return activities
    except Exception as e:
        return f"Error retrieving recent activities: {str(e)}"

# User Profile and Basic Information
@app.tool()
async def get_full_name() -> str:
    """Get user's full name"""
    try:
        name = garmin_client.get_full_name()
        return name
    except Exception as e:
        return f"Error retrieving full name: {str(e)}"

@app.tool()
async def get_unit_system() -> str:
    """Get user's unit system preference"""
    try:
        unit_system = garmin_client.get_unit_system()
        return unit_system
    except Exception as e:
        return f"Error retrieving unit system: {str(e)}"

@app.tool()
async def get_user_profile() -> str:
    """Get all user settings"""
    try:
        profile = garmin_client.get_user_profile()
        return profile
    except Exception as e:
        return f"Error retrieving user profile: {str(e)}"

@app.tool()
async def get_userprofile_settings() -> str:
    """Get user settings"""
    try:
        settings = garmin_client.get_userprofile_settings()
        return settings
    except Exception as e:
        return f"Error retrieving user profile settings: {str(e)}"

# Device Management
@app.tool()
async def get_devices() -> str:
    """Get all available devices for the current user account"""
    try:
        devices = garmin_client.get_devices()
        return devices
    except Exception as e:
        return f"Error retrieving devices: {str(e)}"

@app.tool()
async def get_device_last_used() -> str:
    """Get device last used information"""
    try:
        device_info = garmin_client.get_device_last_used()
        return device_info
    except Exception as e:
        return f"Error retrieving device last used: {str(e)}"

@app.tool()
async def get_device_settings(device_id: str) -> str:
    """Get device settings for a specific device
    
    Args:
        device_id: ID of the device to get settings for
    """
    try:
        settings = garmin_client.get_device_settings(device_id)
        return settings
    except Exception as e:
        return f"Error retrieving device settings: {str(e)}"

@app.tool()
async def get_device_alarms() -> str:
    """Get list of active alarms from all devices"""
    try:
        alarms = garmin_client.get_device_alarms()
        return alarms
    except Exception as e:
        return f"Error retrieving device alarms: {str(e)}"

@app.tool()
async def get_primary_training_device() -> str:
    """Get detailed information about primary training devices"""
    try:
        device_info = garmin_client.get_primary_training_device()
        return device_info
    except Exception as e:
        return f"Error retrieving primary training device: {str(e)}"

# Health and Wellness Data
@app.tool()
async def get_stats(cdate: str) -> str:
    """Get user activity summary for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        stats = garmin_client.get_stats(cdate)
        return stats
    except Exception as e:
        return f"Error retrieving stats: {str(e)}"

@app.tool()
async def get_user_summary(cdate: str) -> str:
    """Get user activity summary for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        summary = garmin_client.get_user_summary(cdate)
        return summary
    except Exception as e:
        return f"Error retrieving user summary: {str(e)}"

@app.tool()
async def get_steps_data(cdate: str) -> str:
    """Get steps data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        steps = garmin_client.get_steps_data(cdate)
        return steps
    except Exception as e:
        return f"Error retrieving steps data: {str(e)}"

@app.tool()
async def get_daily_steps(start: str, end: str) -> str:
    """Get steps data between two dates
    
    Args:
        start: Start date in YYYY-MM-DD format
        end: End date in YYYY-MM-DD format
    """
    try:
        steps = garmin_client.get_daily_steps(start, end)
        return steps
    except Exception as e:
        return f"Error retrieving daily steps: {str(e)}"

@app.tool()
async def get_heart_rates(cdate: str) -> str:
    """Get heart rate data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        heart_rates = garmin_client.get_heart_rates(cdate)
        return heart_rates
    except Exception as e:
        return f"Error retrieving heart rates: {str(e)}"

@app.tool()
async def get_rhr_day(cdate: str) -> str:
    """Get resting heart rate data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        rhr = garmin_client.get_rhr_day(cdate)
        return rhr
    except Exception as e:
        return f"Error retrieving resting heart rate: {str(e)}"

@app.tool()
async def get_hrv_data(cdate: str) -> str:
    """Get Heart Rate Variability (HRV) data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        hrv = garmin_client.get_hrv_data(cdate)
        return hrv
    except Exception as e:
        return f"Error retrieving HRV data: {str(e)}"

@app.tool()
async def get_sleep_data(cdate: str) -> str:
    """Get sleep data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        sleep = garmin_client.get_sleep_data(cdate)
        return sleep
    except Exception as e:
        return f"Error retrieving sleep data: {str(e)}"

@app.tool()
async def get_stress_data(cdate: str) -> str:
    """Get stress data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        stress = garmin_client.get_stress_data(cdate)
        return stress
    except Exception as e:
        return f"Error retrieving stress data: {str(e)}"

@app.tool()
async def get_all_day_stress(cdate: str) -> str:
    """Get all day stress data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        stress = garmin_client.get_all_day_stress(cdate)
        return stress
    except Exception as e:
        return f"Error retrieving all day stress data: {str(e)}"

@app.tool()
async def get_body_battery(startdate: str, enddate: str = None) -> str:
    """Get body battery values between dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format (optional)
    """
    try:
        battery = garmin_client.get_body_battery(startdate, enddate)
        return battery
    except Exception as e:
        return f"Error retrieving body battery data: {str(e)}"

@app.tool()
async def get_body_battery_events(cdate: str) -> str:
    """Get body battery events for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        events = garmin_client.get_body_battery_events(cdate)
        return events
    except Exception as e:
        return f"Error retrieving body battery events: {str(e)}"

@app.tool()
async def get_body_composition(startdate: str, enddate: str = None) -> str:
    """Get body composition data between dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format (optional)
    """
    try:
        composition = garmin_client.get_body_composition(startdate, enddate)
        return composition
    except Exception as e:
        return f"Error retrieving body composition: {str(e)}"

@app.tool()
async def get_stats_and_body(cdate: str) -> str:
    """Get activity data and body composition for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        data = garmin_client.get_stats_and_body(cdate)
        return data
    except Exception as e:
        return f"Error retrieving stats and body data: {str(e)}"

@app.tool()
async def get_hydration_data(cdate: str) -> str:
    """Get hydration data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        hydration = garmin_client.get_hydration_data(cdate)
        return hydration
    except Exception as e:
        return f"Error retrieving hydration data: {str(e)}"

@app.tool()
async def get_respiration_data(cdate: str) -> str:
    """Get respiration data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        respiration = garmin_client.get_respiration_data(cdate)
        return respiration
    except Exception as e:
        return f"Error retrieving respiration data: {str(e)}"

@app.tool()
async def get_spo2_data(cdate: str) -> str:
    """Get SpO2 data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        spo2 = garmin_client.get_spo2_data(cdate)
        return spo2
    except Exception as e:
        return f"Error retrieving SpO2 data: {str(e)}"

@app.tool()
async def get_floors(cdate: str) -> str:
    """Get floors data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        floors = garmin_client.get_floors(cdate)
        return floors
    except Exception as e:
        return f"Error retrieving floors data: {str(e)}"

@app.tool()
async def get_intensity_minutes_data(cdate: str) -> str:
    """Get Intensity Minutes data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        intensity = garmin_client.get_intensity_minutes_data(cdate)
        return intensity
    except Exception as e:
        return f"Error retrieving intensity minutes data: {str(e)}"

@app.tool()
async def get_max_metrics(cdate: str) -> str:
    """Get max metric data (like vo2MaxValue and fitnessAge) for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        metrics = garmin_client.get_max_metrics(cdate)
        return metrics
    except Exception as e:
        return f"Error retrieving max metrics: {str(e)}"

@app.tool()
async def get_fitnessage_data(cdate: str) -> str:
    """Get Fitness Age data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        fitness_age = garmin_client.get_fitnessage_data(cdate)
        return fitness_age
    except Exception as e:
        return f"Error retrieving fitness age data: {str(e)}"

@app.tool()
async def get_training_readiness(cdate: str) -> str:
    """Get training readiness data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        readiness = garmin_client.get_training_readiness(cdate)
        return readiness
    except Exception as e:
        return f"Error retrieving training readiness: {str(e)}"

@app.tool()
async def get_training_status(cdate: str) -> str:
    """Get training status data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        status = garmin_client.get_training_status(cdate)
        return status
    except Exception as e:
        return f"Error retrieving training status: {str(e)}"

@app.tool()
async def get_hill_score(startdate: str, enddate: str = None) -> str:
    """Get hill score data between dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format (optional)
    """
    try:
        hill_score = garmin_client.get_hill_score(startdate, enddate)
        return hill_score
    except Exception as e:
        return f"Error retrieving hill score: {str(e)}"

@app.tool()
async def get_endurance_score(startdate: str, enddate: str = None) -> str:
    """Get endurance score data between dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format (optional)
    """
    try:
        endurance_score = garmin_client.get_endurance_score(startdate, enddate)
        return endurance_score
    except Exception as e:
        return f"Error retrieving endurance score: {str(e)}"

# Weight and Body Composition Management
@app.tool()
async def get_weigh_ins(startdate: str, enddate: str) -> str:
    """Get weigh-ins between two dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format
    """
    try:
        weigh_ins = garmin_client.get_weigh_ins(startdate, enddate)
        return weigh_ins
    except Exception as e:
        return f"Error retrieving weigh-ins: {str(e)}"

@app.tool()
async def get_daily_weigh_ins(cdate: str) -> str:
    """Get weigh-ins for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        weigh_ins = garmin_client.get_daily_weigh_ins(cdate)
        return weigh_ins
    except Exception as e:
        return f"Error retrieving daily weigh-ins: {str(e)}"

@app.tool()
async def add_weigh_in(weight: int, unitKey: str = "kg", timestamp: str = "") -> str:
    """Add a weigh-in
    
    Args:
        weight: Weight value
        unitKey: Unit key (default: kg)
        timestamp: Timestamp (optional)
    """
    try:
        result = garmin_client.add_weigh_in(weight, unitKey, timestamp)
        return f"Successfully added weigh-in: {result}"
    except Exception as e:
        return f"Error adding weigh-in: {str(e)}"

@app.tool()
async def add_weigh_in_with_timestamps(weight: int, unitKey: str = "kg", dateTimestamp: str = "", gmtTimestamp: str = "") -> str:
    """Add a weigh-in with explicit timestamps
    
    Args:
        weight: Weight value
        unitKey: Unit key (default: kg)
        dateTimestamp: Date timestamp (optional)
        gmtTimestamp: GMT timestamp (optional)
    """
    try:
        result = garmin_client.add_weigh_in_with_timestamps(weight, unitKey, dateTimestamp, gmtTimestamp)
        return f"Successfully added weigh-in with timestamps: {result}"
    except Exception as e:
        return f"Error adding weigh-in with timestamps: {str(e)}"

@app.tool()
async def delete_weigh_ins(cdate: str, delete_all: bool = False) -> str:
    """Delete weigh-ins for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
        delete_all: Whether to delete all weigh-ins for that date (default: False)
    """
    try:
        result = garmin_client.delete_weigh_ins(cdate, delete_all)
        return f"Successfully deleted weigh-ins: {result}"
    except Exception as e:
        return f"Error deleting weigh-ins: {str(e)}"

@app.tool()
async def delete_weigh_in(weight_pk: str, cdate: str) -> str:
    """Delete a specific weigh-in
    
    Args:
        weight_pk: Weight primary key
        cdate: Date in YYYY-MM-DD format
    """
    try:
        result = garmin_client.delete_weigh_in(weight_pk, cdate)
        return f"Successfully deleted weigh-in: {result}"
    except Exception as e:
        return f"Error deleting weigh-in: {str(e)}"

@app.tool()
async def add_body_composition(timestamp: str, weight: float, percent_fat: float = None, percent_hydration: float = None, 
                              visceral_fat_mass: float = None, bone_mass: float = None, muscle_mass: float = None, 
                              basal_met: float = None, active_met: float = None, physique_rating: float = None, 
                              metabolic_age: float = None, visceral_fat_rating: float = None, bmi: float = None) -> str:
    """Add body composition data
    
    Args:
        timestamp: Timestamp for the measurement
        weight: Weight value
        percent_fat: Percent body fat (optional)
        percent_hydration: Percent hydration (optional)
        visceral_fat_mass: Visceral fat mass (optional)
        bone_mass: Bone mass (optional)
        muscle_mass: Muscle mass (optional)
        basal_met: Basal metabolic rate (optional)
        active_met: Active metabolic rate (optional)
        physique_rating: Physique rating (optional)
        metabolic_age: Metabolic age (optional)
        visceral_fat_rating: Visceral fat rating (optional)
        bmi: BMI (optional)
    """
    try:
        result = garmin_client.add_body_composition(timestamp, weight, percent_fat, percent_hydration, 
                                                   visceral_fat_mass, bone_mass, muscle_mass, basal_met, 
                                                   active_met, physique_rating, metabolic_age, visceral_fat_rating, bmi)
        return f"Successfully added body composition: {result}"
    except Exception as e:
        return f"Error adding body composition: {str(e)}"

@app.tool()
async def add_hydration_data(value_in_ml: float, timestamp: str = None, cdate: str = None) -> str:
    """Add hydration data in ml
    
    Args:
        value_in_ml: The number of ml of water to add (positive) or subtract (negative)
        timestamp: The timestamp of the hydration update (optional)
        cdate: The date of the hydration update (optional)
    """
    try:
        result = garmin_client.add_hydration_data(value_in_ml, timestamp, cdate)
        return f"Successfully added hydration data: {result}"
    except Exception as e:
        return f"Error adding hydration data: {str(e)}"

# Blood Pressure and Medical Data
@app.tool()
async def get_blood_pressure(startdate: str, enddate: str = None) -> str:
    """Get blood pressure data between dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format (optional)
    """
    try:
        bp = garmin_client.get_blood_pressure(startdate, enddate)
        return bp
    except Exception as e:
        return f"Error retrieving blood pressure data: {str(e)}"

@app.tool()
async def set_blood_pressure(systolic: int, diastolic: int, pulse: int, timestamp: str = "", notes: str = "") -> str:
    """Add blood pressure measurement
    
    Args:
        systolic: Systolic blood pressure
        diastolic: Diastolic blood pressure
        pulse: Pulse rate
        timestamp: Timestamp (optional)
        notes: Notes (optional)
    """
    try:
        result = garmin_client.set_blood_pressure(systolic, diastolic, pulse, timestamp, notes)
        return f"Successfully added blood pressure: {result}"
    except Exception as e:
        return f"Error adding blood pressure: {str(e)}"

@app.tool()
async def delete_blood_pressure(version: str, cdate: str) -> str:
    """Delete specific blood pressure measurement
    
    Args:
        version: Version of the blood pressure measurement
        cdate: Date in YYYY-MM-DD format
    """
    try:
        result = garmin_client.delete_blood_pressure(version, cdate)
        return f"Successfully deleted blood pressure: {result}"
    except Exception as e:
        return f"Error deleting blood pressure: {str(e)}"

@app.tool()
async def get_menstrual_calendar_data(startdate: str, enddate: str) -> str:
    """Get menstrual calendar data between dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format
    """
    try:
        menstrual_data = garmin_client.get_menstrual_calendar_data(startdate, enddate)
        return menstrual_data
    except Exception as e:
        return f"Error retrieving menstrual calendar data: {str(e)}"

@app.tool()
async def get_menstrual_data_for_date(fordate: str) -> str:
    """Get menstrual data for a specific date
    
    Args:
        fordate: Date in YYYY-MM-DD format
    """
    try:
        menstrual_data = garmin_client.get_menstrual_data_for_date(fordate)
        return menstrual_data
    except Exception as e:
        return f"Error retrieving menstrual data: {str(e)}"

@app.tool()
async def get_pregnancy_summary() -> str:
    """Get pregnancy summary data"""
    try:
        pregnancy_data = garmin_client.get_pregnancy_summary()
        return pregnancy_data
    except Exception as e:
        return f"Error retrieving pregnancy summary: {str(e)}"

# Gear and Equipment Management
@app.tool()
async def get_gear(userProfileNumber: int) -> str:
    """Get all user gear
    
    Args:
        userProfileNumber: User profile number
    """
    try:
        gear = garmin_client.get_gear(userProfileNumber)
        return gear
    except Exception as e:
        return f"Error retrieving gear: {str(e)}"

@app.tool()
async def get_gear_defaults(userProfileNumber: int) -> str:
    """Get gear defaults for a user profile
    
    Args:
        userProfileNumber: User profile number
    """
    try:
        defaults = garmin_client.get_gear_defaults(userProfileNumber)
        return defaults
    except Exception as e:
        return f"Error retrieving gear defaults: {str(e)}"

@app.tool()
async def get_gear_ativities(gearUUID: str, limit: int = 9999) -> str:
    """Get activities where specific gear was used
    
    Args:
        gearUUID: UUID of the gear to get activities for
        limit: Maximum number of activities to return (default: 9999)
    """
    try:
        activities = garmin_client.get_gear_ativities(gearUUID, limit)
        return activities
    except Exception as e:
        return f"Error retrieving gear activities: {str(e)}"

@app.tool()
async def get_gear_stats(gearUUID: str) -> str:
    """Get statistics for specific gear
    
    Args:
        gearUUID: UUID of the gear to get stats for
    """
    try:
        stats = garmin_client.get_gear_stats(gearUUID)
        return stats
    except Exception as e:
        return f"Error retrieving gear stats: {str(e)}"

@app.tool()
async def set_gear_default(activityType: str, gearUUID: str, defaultGear: bool = True) -> str:
    """Set gear as default for an activity type
    
    Args:
        activityType: Type of activity
        gearUUID: UUID of the gear
        defaultGear: Whether to set as default (default: True)
    """
    try:
        result = garmin_client.set_gear_default(activityType, gearUUID, defaultGear)
        return f"Successfully set gear default: {result}"
    except Exception as e:
        return f"Error setting gear default: {str(e)}"

# Goals and Challenges
@app.tool()
async def get_goals(status: str = "active", start: int = 1, limit: int = 30) -> str:
    """Get goals based on status
    
    Args:
        status: Status of goals (active, future, or past) (default: active)
        start: Initial goal index (default: 1)
        limit: Pagination limit (default: 30)
    """
    try:
        goals = garmin_client.get_goals(status, start, limit)
        return goals
    except Exception as e:
        return f"Error retrieving goals: {str(e)}"

@app.tool()
async def get_adhoc_challenges(start: int, limit: int) -> str:
    """Get adhoc challenges for current user
    
    Args:
        start: Starting index
        limit: Number of challenges to return
    """
    try:
        challenges = garmin_client.get_adhoc_challenges(start, limit)
        return challenges
    except Exception as e:
        return f"Error retrieving adhoc challenges: {str(e)}"

@app.tool()
async def get_available_badge_challenges(start: int, limit: int) -> str:
    """Get available badge challenges
    
    Args:
        start: Starting index
        limit: Number of challenges to return
    """
    try:
        challenges = garmin_client.get_available_badge_challenges(start, limit)
        return challenges
    except Exception as e:
        return f"Error retrieving available badge challenges: {str(e)}"

@app.tool()
async def get_badge_challenges(start: int, limit: int) -> str:
    """Get badge challenges for current user
    
    Args:
        start: Starting index
        limit: Number of challenges to return
    """
    try:
        challenges = garmin_client.get_badge_challenges(start, limit)
        return challenges
    except Exception as e:
        return f"Error retrieving badge challenges: {str(e)}"

@app.tool()
async def get_non_completed_badge_challenges(start: int, limit: int) -> str:
    """Get non-completed badge challenges for current user
    
    Args:
        start: Starting index
        limit: Number of challenges to return
    """
    try:
        challenges = garmin_client.get_non_completed_badge_challenges(start, limit)
        return challenges
    except Exception as e:
        return f"Error retrieving non-completed badge challenges: {str(e)}"

@app.tool()
async def get_earned_badges() -> str:
    """Get earned badges for current user"""
    try:
        badges = garmin_client.get_earned_badges()
        return badges
    except Exception as e:
        return f"Error retrieving earned badges: {str(e)}"

@app.tool()
async def get_personal_record() -> str:
    """Get personal records for current user"""
    try:
        records = garmin_client.get_personal_record()
        return records
    except Exception as e:
        return f"Error retrieving personal records: {str(e)}"

@app.tool()
async def get_inprogress_virtual_challenges(start: int, limit: int) -> str:
    """Get in-progress virtual challenges for current user
    
    Args:
        start: Starting index
        limit: Number of challenges to return
    """
    try:
        challenges = garmin_client.get_inprogress_virtual_challenges(start, limit)
        return challenges
    except Exception as e:
        return f"Error retrieving in-progress virtual challenges: {str(e)}"

# Workouts and Training
@app.tool()
async def get_workouts(start: int = 0, end: int = 100) -> str:
    """Get workouts from start to end
    
    Args:
        start: Starting index (default: 0)
        end: Ending index (default: 100)
    """
    try:
        workouts = garmin_client.get_workouts(start, end)
        return workouts
    except Exception as e:
        return f"Error retrieving workouts: {str(e)}"

@app.tool()
async def get_workout_by_id(workout_id: int) -> str:
    """Get workout by ID
    
    Args:
        workout_id: ID of the workout to retrieve
    """
    try:
        workout = garmin_client.get_workout_by_id(workout_id)
        return workout
    except Exception as e:
        return f"Error retrieving workout: {str(e)}"

@app.tool()
async def download_workout(workout_id: int) -> str:
    """Download workout by ID
    
    Args:
        workout_id: ID of the workout to download
    """
    try:
        workout_data = garmin_client.download_workout(workout_id)
        return f"Successfully downloaded workout {workout_id}"
    except Exception as e:
        return f"Error downloading workout: {str(e)}"

@app.tool()
async def get_race_predictions(startdate: str = None, enddate: str = None, _type: str = None) -> str:
    """Get race predictions for 5k, 10k, half marathon and marathon
    
    Args:
        startdate: Start date in YYYY-MM-DD format (optional)
        enddate: End date in YYYY-MM-DD format (optional)
        _type: Type of prediction (daily or monthly) (optional)
    """
    try:
        predictions = garmin_client.get_race_predictions(startdate, enddate, _type)
        return predictions
    except Exception as e:
        return f"Error retrieving race predictions: {str(e)}"

@app.tool()
async def get_progress_summary_between_dates(startdate: str, enddate: str, metric: str = "distance", groupbyactivities: bool = True) -> str:
    """Get progress summary data between specific dates
    
    Args:
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format
        metric: Metric to calculate (elevationGain, duration, distance, movingDuration) (default: distance)
        groupbyactivities: Group summary by activity type (default: True)
    """
    try:
        summary = garmin_client.get_progress_summary_between_dates(startdate, enddate, metric, groupbyactivities)
        return summary
    except Exception as e:
        return f"Error retrieving progress summary: {str(e)}"

# Activity Management and Upload/Download
@app.tool()
async def get_last_activity() -> str:
    """Get the last activity"""
    try:
        activity = garmin_client.get_last_activity()
        return activity
    except Exception as e:
        return f"Error retrieving last activity: {str(e)}"

@app.tool()
async def get_activity_details(activity_id: int, maxchart: int = 2000, maxpoly: int = 4000) -> str:
    """Get detailed activity information
    
    Args:
        activity_id: ID of the activity
        maxchart: Maximum chart data points (default: 2000)
        maxpoly: Maximum polygon data points (default: 4000)
    """
    try:
        details = garmin_client.get_activity_details(activity_id, maxchart, maxpoly)
        return details
    except Exception as e:
        return f"Error retrieving activity details: {str(e)}"

@app.tool()
async def get_activity_types() -> str:
    """Get available activity types"""
    try:
        types = garmin_client.get_activity_types()
        return types
    except Exception as e:
        return f"Error retrieving activity types: {str(e)}"

@app.tool()
async def download_activity(activity_id: int, dl_fmt: int = 2) -> str:
    """Download activity in requested format
    
    Args:
        activity_id: ID of the activity to download
        dl_fmt: Download format (default: 2 for TCX)
    """
    try:
        activity_data = garmin_client.download_activity(activity_id, dl_fmt)
        return f"Successfully downloaded activity {activity_id}"
    except Exception as e:
        return f"Error downloading activity: {str(e)}"

@app.tool()
async def upload_activity(activity_path: str) -> str:
    """Upload activity in FIT format from file
    
    Args:
        activity_path: Path to the activity file
    """
    try:
        result = garmin_client.upload_activity(activity_path)
        return f"Successfully uploaded activity: {result}"
    except Exception as e:
        return f"Error uploading activity: {str(e)}"

@app.tool()
async def delete_activity(activity_id: int) -> str:
    """Delete activity with specified ID
    
    Args:
        activity_id: ID of the activity to delete
    """
    try:
        result = garmin_client.delete_activity(activity_id)
        return f"Successfully deleted activity {activity_id}"
    except Exception as e:
        return f"Error deleting activity: {str(e)}"

@app.tool()
async def set_activity_name(activity_id: int, title: str) -> str:
    """Set name for activity with ID
    
    Args:
        activity_id: ID of the activity
        title: New title for the activity
    """
    try:
        result = garmin_client.set_activity_name(activity_id, title)
        return f"Successfully set activity name: {result}"
    except Exception as e:
        return f"Error setting activity name: {str(e)}"

@app.tool()
async def set_activity_type(activity_id: int, type_id: int, type_key: str, parent_type_id: int) -> str:
    """Set activity type
    
    Args:
        activity_id: ID of the activity
        type_id: Type ID
        type_key: Type key
        parent_type_id: Parent type ID
    """
    try:
        result = garmin_client.set_activity_type(activity_id, type_id, type_key, parent_type_id)
        return f"Successfully set activity type: {result}"
    except Exception as e:
        return f"Error setting activity type: {str(e)}"

@app.tool()
async def create_manual_activity(start_datetime: str, timezone: str, type_key: str, distance_km: float, duration_min: int, activity_name: str) -> str:
    """Create a manual activity
    
    Args:
        start_datetime: Start datetime in format "2023-12-02T10:00:00.00"
        timezone: Local timezone (e.g., 'Europe/Paris')
        type_key: Activity type key (e.g., 'resort_skiing')
        distance_km: Distance in kilometers
        duration_min: Duration in minutes
        activity_name: Activity title
    """
    try:
        result = garmin_client.create_manual_activity(start_datetime, timezone, type_key, distance_km, duration_min, activity_name)
        return f"Successfully created manual activity: {result}"
    except Exception as e:
        return f"Error creating manual activity: {str(e)}"

@app.tool()
async def create_manual_activity_from_json(payload: dict) -> str:
    """Create a manual activity from JSON payload
    
    Args:
        payload: JSON payload for the activity
    """
    try:
        result = garmin_client.create_manual_activity_from_json(payload)
        return f"Successfully created manual activity from JSON: {result}"
    except Exception as e:
        return f"Error creating manual activity from JSON: {str(e)}"

# Utility and System Methods
@app.tool()
async def get_device_solar_data(device_id: str, startdate: str, enddate: str = None) -> str:
    """Get solar data for compatible device
    
    Args:
        device_id: ID of the device
        startdate: Start date in YYYY-MM-DD format
        enddate: End date in YYYY-MM-DD format (optional)
    """
    try:
        solar_data = garmin_client.get_device_solar_data(device_id, startdate, enddate)
        return solar_data
    except Exception as e:
        return f"Error retrieving device solar data: {str(e)}"

@app.tool()
async def get_all_day_events(cdate: str) -> str:
    """Get available daily events data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        events = garmin_client.get_all_day_events(cdate)
        return events
    except Exception as e:
        return f"Error retrieving all day events: {str(e)}"

@app.tool()
async def get_daily_wellness_events_data(startdate: str) -> str:
    """Get daily wellness events data for a specific date
    
    Args:
        startdate: Date in YYYY-MM-DD format
    """
    try:
        events = garmin_client.get_daily_wellness_events_data(startdate)
        return events
    except Exception as e:
        return f"Error retrieving daily wellness events: {str(e)}"

@app.tool()
async def request_reload(cdate: str) -> str:
    """Request reload of data for a specific date
    
    Args:
        cdate: Date in YYYY-MM-DD format
    """
    try:
        result = garmin_client.request_reload(cdate)
        return f"Successfully requested reload for {cdate}"
    except Exception as e:
        return f"Error requesting reload: {str(e)}"

@app.tool()
async def query_garmin_graphql(query: dict) -> str:
    """Query Garmin GraphQL endpoints
    
    Args:
        query: GraphQL query dictionary
    """
    try:
        result = garmin_client.query_garmin_graphql(query)
        return result
    except Exception as e:
        return f"Error querying GraphQL: {str(e)}"

@app.tool()
async def logout() -> str:
    """Log user out of session"""
    try:
        garmin_client.logout()
        return "Successfully logged out"
    except Exception as e:
        return f"Error logging out: {str(e)}"

if __name__ == "__main__":
    app.run()


