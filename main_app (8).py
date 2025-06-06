import streamlit as st

# Import modules
import memberships_tool as memberships
import membership_credit_tracker as credit_tracker
import membership_insights_ai as member_ai
import facility_membership_monitor as member_benchmark

import dome_usage_tool as usage
import complex_usage_optimizer as optimizer
import visual_calendar_layout as layout
import revenue_heatmap as heatmap
import ai_scheduling_suggestions as schedule_ai
import dynamic_pricing_tool as pricing

import sponsor_dashboard as sponsors
import sponsorship_ai_calculator as sponsor_calc
import pandadoc_contract as pandadoc
import proposal_to_pdf as proposal
import sponsorship_roi_tracker as sponsor_roi

import contract_usage_tracker as contract_tracker
import contract_insights_ai as contract_ai
import facility_contract_monitor as contract_benchmark

import governance_tool as governance
import student_committee as student
import mentorship_center as mentorship
import scholarship_tracker as scholarships

import volunteer_hub as volunteer
import referee_manager as referee
import team_club_manager as teams
import league_coordinator as leagues

import nil_tracker as nil
import ai_matchmaker_tool as matchmaker
import ai_scheduler_tool as scheduler

import central_dashboard as dashboard

st.set_page_config(page_title="Venture North Admin", layout="wide")
st.sidebar.title("🏟️ Venture North Admin")

# Sidebar structure
sections = {
    "📊 Central Dashboard": {"Dashboard Overview": dashboard},
    "👥 Memberships": {
        "Member Manager": memberships,
        "Credit Tracker": credit_tracker,
        "AI Insights": member_ai,
        "Benchmark Monitor": member_benchmark,
    },
    "🏟️ Dome Usage": {
        "Usage Logger": usage,
        "AI Optimizer": optimizer,
        "Visual Layout": layout,
        "Revenue Heatmap": heatmap,
        "AI Scheduling": schedule_ai,
        "Dynamic Pricing": pricing,
    },
    "💼 Sponsorship": {
        "Sponsor Dashboard": sponsors,
        "AI Sponsorship Calculator": sponsor_calc,
        "Contract Generator": pandadoc,
        "Proposal to PDF": proposal,
        "ROI Tracker": sponsor_roi,
    },
    "📑 Contracts & Orgs": {
        "Usage Tracker": contract_tracker,
        "AI Contract Insights": contract_ai,
        "Benchmark Monitor": contract_benchmark,
    },
    "🏛️ Governance": {
        "Board Dashboard": governance,
        "Student Committee": student,
        "Mentorship Center": mentorship,
        "Scholarship Tracker": scholarships,
    },
    "🤝 Personnel": {
        "Volunteer Hub": volunteer,
        "Referee Manager": referee,
        "Teams & Clubs": teams,
        "League Coordinator": leagues,
    },
    "📢 NIL & AI Tools": {
        "NIL Tracker": nil,
        "AI Matchmaker": matchmaker,
        "AI Scheduler": scheduler,
    }
}

section = st.sidebar.selectbox("Select Section", list(sections.keys()))
tool = st.sidebar.selectbox("Select Tool", list(sections[section].keys()))
sections[section][tool].run()