# Garmin Connect MCP Server

A comprehensive FastMCP server that provides access to all Garmin Connect data and functionality through the Model Context Protocol (MCP).

## Features

This server provides tools for accessing and managing all aspects of your Garmin Connect data:

### User Profile and Basic Information
- `get_full_name()` - Get user's full name
- `get_unit_system()` - Get user's unit system preference
- `get_user_profile()` - Get all user settings
- `get_userprofile_settings()` - Get user settings

### Device Management
- `get_devices()` - Get all available devices
- `get_device_last_used()` - Get device last used information
- `get_device_settings(device_id)` - Get device settings for a specific device
- `get_device_alarms()` - Get list of active alarms from all devices
- `get_primary_training_device()` - Get detailed information about primary training devices
- `get_device_solar_data(device_id, startdate, enddate)` - Get solar data for compatible devices

### Health and Wellness Data
- `get_stats(cdate)` - Get user activity summary for a specific date
- `get_user_summary(cdate)` - Get user activity summary for a specific date
- `get_steps_data(cdate)` - Get steps data for a specific date
- `get_daily_steps(start, end)` - Get steps data between two dates
- `get_heart_rates(cdate)` - Get heart rate data for a specific date
- `get_rhr_day(cdate)` - Get resting heart rate data for a specific date
- `get_hrv_data(cdate)` - Get Heart Rate Variability (HRV) data for a specific date
- `get_sleep_data(cdate)` - Get sleep data for a specific date
- `get_stress_data(cdate)` - Get stress data for a specific date
- `get_all_day_stress(cdate)` - Get all day stress data for a specific date
- `get_body_battery(startdate, enddate)` - Get body battery values between dates
- `get_body_battery_events(cdate)` - Get body battery events for a specific date
- `get_body_composition(startdate, enddate)` - Get body composition data between dates
- `get_stats_and_body(cdate)` - Get activity data and body composition for a specific date
- `get_hydration_data(cdate)` - Get hydration data for a specific date
- `get_respiration_data(cdate)` - Get respiration data for a specific date
- `get_spo2_data(cdate)` - Get SpO2 data for a specific date
- `get_floors(cdate)` - Get floors data for a specific date
- `get_intensity_minutes_data(cdate)` - Get Intensity Minutes data for a specific date
- `get_max_metrics(cdate)` - Get max metric data (like vo2MaxValue and fitnessAge)
- `get_fitnessage_data(cdate)` - Get Fitness Age data for a specific date
- `get_training_readiness(cdate)` - Get training readiness data for a specific date
- `get_training_status(cdate)` - Get training status data for a specific date
- `get_hill_score(startdate, enddate)` - Get hill score data between dates
- `get_endurance_score(startdate, enddate)` - Get endurance score data between dates

### Weight and Body Composition Management
- `get_weigh_ins(startdate, enddate)` - Get weigh-ins between two dates
- `get_daily_weigh_ins(cdate)` - Get weigh-ins for a specific date
- `add_weigh_in(weight, unitKey, timestamp)` - Add a weigh-in
- `add_weigh_in_with_timestamps(weight, unitKey, dateTimestamp, gmtTimestamp)` - Add a weigh-in with explicit timestamps
- `delete_weigh_ins(cdate, delete_all)` - Delete weigh-ins for a specific date
- `delete_weigh_in(weight_pk, cdate)` - Delete a specific weigh-in
- `add_body_composition(timestamp, weight, ...)` - Add body composition data
- `add_hydration_data(value_in_ml, timestamp, cdate)` - Add hydration data in ml

### Blood Pressure and Medical Data
- `get_blood_pressure(startdate, enddate)` - Get blood pressure data between dates
- `set_blood_pressure(systolic, diastolic, pulse, timestamp, notes)` - Add blood pressure measurement
- `delete_blood_pressure(version, cdate)` - Delete specific blood pressure measurement
- `get_menstrual_calendar_data(startdate, enddate)` - Get menstrual calendar data between dates
- `get_menstrual_data_for_date(fordate)` - Get menstrual data for a specific date
- `get_pregnancy_summary()` - Get pregnancy summary data

### Gear and Equipment Management
- `get_gear(userProfileNumber)` - Get all user gear
- `get_gear_defaults(userProfileNumber)` - Get gear defaults for a user profile
- `get_gear_ativities(gearUUID, limit)` - Get activities where specific gear was used
- `get_gear_stats(gearUUID)` - Get statistics for specific gear
- `set_gear_default(activityType, gearUUID, defaultGear)` - Set gear as default for an activity type

### Goals and Challenges
- `get_goals(status, start, limit)` - Get goals based on status
- `get_adhoc_challenges(start, limit)` - Get adhoc challenges for current user
- `get_available_badge_challenges(start, limit)` - Get available badge challenges
- `get_badge_challenges(start, limit)` - Get badge challenges for current user
- `get_non_completed_badge_challenges(start, limit)` - Get non-completed badge challenges for current user
- `get_earned_badges()` - Get earned badges for current user
- `get_personal_record()` - Get personal records for current user
- `get_inprogress_virtual_challenges(start, limit)` - Get in-progress virtual challenges for current user

### Workouts and Training
- `get_workouts(start, end)` - Get workouts from start to end
- `get_workout_by_id(workout_id)` - Get workout by ID
- `download_workout(workout_id)` - Download workout by ID
- `get_race_predictions(startdate, enddate, _type)` - Get race predictions for 5k, 10k, half marathon and marathon
- `get_progress_summary_between_dates(startdate, enddate, metric, groupbyactivities)` - Get progress summary data between specific dates

### Activity Management and Upload/Download
- `get_activities(start, limit, activitytype)` - Get recent activities
- `get_activities_by_date(startdate, enddate, activitytype, sortorder)` - Get activities between specific dates
- `get_activities_fordate(fordate)` - Get activities for a specific date
- `get_activity(activity_id)` - Get basic activity information
- `get_last_activity()` - Get the last activity
- `get_activity_details(activity_id, maxchart, maxpoly)` - Get detailed activity information
- `get_activity_splits(activity_id)` - Get splits for an activity
- `get_activity_typed_splits(activity_id)` - Get typed splits for an activity
- `get_activity_split_summaries(activity_id)` - Get split summaries for an activity
- `get_activity_weather(activity_id)` - Get weather data for an activity
- `get_activity_hr_in_timezones(activity_id)` - Get heart rate data in different time zones for an activity
- `get_activity_gear(activity_id)` - Get gear data used for an activity
- `get_activity_exercise_sets(activity_id)` - Get exercise sets for strength training activities
- `get_activity_types()` - Get available activity types
- `download_activity(activity_id, dl_fmt)` - Download activity in requested format
- `upload_activity(activity_path)` - Upload activity in FIT format from file
- `delete_activity(activity_id)` - Delete activity with specified ID
- `set_activity_name(activity_id, title)` - Set name for activity with ID
- `set_activity_type(activity_id, type_id, type_key, parent_type_id)` - Set activity type
- `create_manual_activity(start_datetime, timezone, type_key, distance_km, duration_min, activity_name)` - Create a manual activity
- `create_manual_activity_from_json(payload)` - Create a manual activity from JSON payload

### Utility and System Methods
- `get_all_day_events(cdate)` - Get available daily events data for a specific date
- `get_daily_wellness_events_data(startdate)` - Get daily wellness events data for a specific date
- `request_reload(cdate)` - Request reload of data for a specific date
- `query_garmin_graphql(query)` - Query Garmin GraphQL endpoints
- `logout()` - Log user out of session

### Usage
The server will start and be available for MCP clients to connect to. All tools are automatically available and can be called with appropriate parameters.

## Configuration
Update the following variables in a .env:
- `GARMIN_EMAIL`: Your Garmin Connect email
- `GARMIN_PASSWORD`: Your Garmin Connect password

## Notes
- The server uses the Garmin Connect Python library for authentication and data access
- All date parameters should be in YYYY-MM-DD format
- Activity IDs can be obtained from the activity list methods
- Some methods may require specific device types or data availability

