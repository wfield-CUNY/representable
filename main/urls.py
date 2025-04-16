#
# Copyright (c) 2019- Representable Team (Theodor Marcu, Lauren Johnston, Somya Arora, Kyle Barnes, Preeti Iyer).
#
# This file is part of Representable
# (see http://representable.org).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
from django.urls import include, path

from main.views import main, partners, dashboard, drives
from main.views.dashboard import AllowListUpdate, AllowListManage, AllowListDelete
from representable.settings.base import MAPBOX_KEY

app_name = "main"
urlpatterns = [
    
    path(
        "accounts/login/",
        main.RepresentableLoginView.as_view(),
        name="account_login",
    ),
    path(
        "accounts/signup/",
        main.RepresentableSignupView.as_view(),
        name="account_signup",
    ),

    # google code comment
    # path(
    #     "accounts/social/signup/",
    #     views.main.RepresentableSocialSignupView.as_view(),
    #     name="socialaccount_signup",
    # ),

    path(
        'block_group_polygons/<str:abbr>/',
        main.block_group_polygons,
        name='block_group_polygons',
    ),
    path("", main.Index.as_view(), name="index"),
    path(
        "entry_preview/",
        main.StateSelection.as_view(),
        name="entry_preview",
    ),
    path(
        "state_selection/",
        main.StateSelection.as_view(),
        name="state_selection",
    ),
    path(
        "state_selection/map",
        main.StateSelection.as_view(),
        name="state_selection_map",
    ),
    path(
        "entry/",
        main.EntryView.as_view(),
        {"token": "", "drive": ""},
        name="entry",
    ),
    path(
        "entry/drive/<slug:drive>/",
        main.EntryView.as_view(),
        {"token": "", "abbr": ""},
        name="entry",  # deprecated? every drive page should redirect to incl. abbr
    ),
    path(
        "entry/drive/<slug:drive>/<abbr>",
        main.EntryView.as_view(),
        {"token": ""},
        name="entry",
    ),
    path(
        "entry/c/<slug:drive>/",
        main.EntryView.as_view(),
        {"token": ""},
        name="entry_legacy",  # for old links
    ),
    path(
        "entry/t/<token>/",
        main.EntryView.as_view(),
        {"drive": ""},
        name="entry",
    ),
    path(
        "entry/t/<token>/<abbr>/",
        main.EntryView.as_view(),
        {"drive": ""},
        name="entry",
    ),
    path(
        "entry/<abbr>/",
        main.EntryView.as_view(),
        {"token": "", "state": "", "drive": ""},
        name="entry",
    ),
    path("about/", main.About.as_view(), name="about"),
    path("faq/", main.FAQ.as_view(), name="faq"),
    path("glossary/", main.Glossary.as_view(), name="glossary"),
    path("resources/", main.Resources.as_view(), name="resources"),
    path("resources/<abbr>/", main.Resources.as_view(), {"state": ""}, name="resources"),
    path("review/", main.Review.as_view(), name="review"),
    path("privacy/", main.Privacy.as_view(), name="privacy"),
    path("terms/", main.Terms.as_view(), name="terms"),
    path("state/<abbr>/", main.StatePage.as_view(), name="state"),
    path(
        "submission/<map_id>",
        main.Submission.as_view(),
        {"slug": "", "drive": ""},
        name="submission",
    ),
    path(
        "submission/<map_id>/<abbr>",
        main.Submission.as_view(),
        {"slug": "", "drive": ""},
        name="submission",
    ),
    path(
        "submission/thanks/<map_id>/<abbr>",
        main.Submission.as_view(),
        {"slug": "", "drive": ""},
        name="submission_thanks",
    ),
    path(
        "submission/thanks/drive/<slug:slug>/<slug:drive>/<map_id>",
        main.Submission.as_view(),
        name="submission_thanks",
    ),
    # path("blog/", views.main.Blog.as_view(), name="blog"),
    path("export/geojson/", main.ExportView.as_view(), name="export"),
    path("export/csv/", main.ExportView.as_view(), name="export"),
    path("export/geojson/<abbr>/", main.ExportView.as_view(), name="export"),
    path("export/csv/<abbr>/", main.ExportView.as_view(), name="export"),
    path(
        "multiexport/<abbr>/<type>/",
        main.MultiExportView.as_view(),
        name="multi_export",
    ),
    path(
        "multiexport/drive/<drive>/<type>/",
        partners.MultiExportView.as_view(),
        name="multi_export",
    ),
    path(
        "multiexport/org/<org>/<type>/",
        partners.MultiExportView.as_view(),
        name="multi_export",
    ),
    path("partners/", partners.IndexView.as_view(), name="partner_list"),
    path(
        "partners/welcome/",
        partners.WelcomeView.as_view(),
        name="partner_welcome",
    ),
    path(
        "partners/<slug:slug>/",
        partners.PartnerView.as_view(),
        name="partner_page",
    ),
    path("map/<state>/", main.Map.as_view(), name="map"),
    path("map/<state>/<lat>/<lng>", main.Map.as_view(), name="map"),
    path(
        "map/p/<slug:slug>/",
        partners.PartnerMap.as_view(),
        {"drive": ""},
        name="partner_map",
    ),
    path(
        "map/p/<slug:slug>/<slug:drive>/",
        partners.PartnerMap.as_view(),
        name="partner_map",
    ),
    path(
        "report/",
        partners.ReportView.as_view(),
        name="report_community",
    ),
    path(
        "drive/<slug:slug>/",
        drives.DriveView.as_view(),
        name="drive_page",
    ),
    # keeping this for now to maintain link to user testing campaign
    path(
        "c/<slug:slug>/",
        drives.DriveView.as_view(),
        name="drive_page_legacy",
    ),
    path("dashboard/", dashboard.IndexView.as_view(), name="dashboard"),
    path(
        "dashboard/entries/<int:pk>",
        dashboard.ViewEntry.as_view(),
        name="dash_entry_list",
    ),
    path(
        "dashboard/entries/<int:pk>",
        dashboard.ViewEntry.as_view(),
        name="dash_view_entry",
    ),
    path(
        "dashboard/entries/<int:pk>/delete/",
        dashboard.DeleteEntry.as_view(),
        name="dash_delete_entry",
    ),
    path(
        "dashboard/partners/create/",
        dashboard.CreateOrg.as_view(),
        name="create_org",
    ),
    path(
        "dashboard/partners/<slug:slug>-<int:pk>/",
        include(
            [
                path("", dashboard.HomeOrg.as_view(), name="home_org"),
                path(
                    "thanks/",
                    dashboard.ThanksOrg.as_view(),
                    name="thanks_org",
                ),
                path(
                    "edit/", dashboard.EditOrg.as_view(), name="edit_org"
                ),
                path(
                    "delete/",
                    dashboard.DeleteOrg.as_view(),
                    name="delete_org",
                ),
                path(
                    "members/",
                    dashboard.ManageOrg.as_view(),
                    name="manage_org",
                ),
                path(
                    "members/create",
                    dashboard.CreateMember.as_view(),
                    name="create_member",
                ),
                path(
                    "drives/create/",
                    dashboard.CreateDrive.as_view(),
                    name="create_drive",
                ),
                path(
                    "drives/<uuid:cam_pk>/",
                    dashboard.DriveHome.as_view(),
                    name="drive_home",
                ),
                path(
                    "drives/<uuid:cam_pk>/edit/",
                    dashboard.UpdateDrive.as_view(),
                    name="update_drive",
                ),
                path(
                    "drives/<uuid:cam_pk>/delete/",
                    dashboard.DeleteDrive.as_view(),
                    name="delete_drive",
                ),
                path(
                    "drives/<uuid:cam_pk>/upload-allowlist/",
                    AllowListUpdate.as_view(),
                    name="upload_allowlist",
                ),
                path(
                    "drives/<uuid:cam_pk>/manage-allowlist/",
                    AllowListManage.as_view(),
                    name="manage_allowlist",
                ),
                path(
                    "drives/<uuid:cam_pk>/manage-allowlist/delete/",
                    AllowListDelete.as_view(),
                    name="delete_allowlist",
                ),
            ]
        ),
    ),
]
