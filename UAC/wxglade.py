#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.9.3 on Fri May 31 07:38:55 2019
#

import wx
import wx.adv

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class _715811673__883977639__931769938_root_frame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: _715811673__883977639__931769938_root_frame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.BORDER_SIMPLE | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((720, 420))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Quit", "Quit the application")
        self.Bind(wx.EVT_MENU, self.quit, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Help", "Try documentation and tutorials")
        self.Bind(wx.EVT_MENU, self.documentation_help, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Report Bugs", "Report bugs to Team dtoxd ")
        self.Bind(wx.EVT_MENU, self.report_bugs, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "Check for Updates", "Check for Updates")
        self.Bind(wx.EVT_MENU, self.check_for_updates, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, "About dtoxd", "Learn more about dtoxd")
        self.Bind(wx.EVT_MENU, self.about_dtoxd, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "About")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.frame_statusbar = self.CreateStatusBar(1, wx.STB_ELLIPSIZE_MIDDLE)
        self.radio_btn_4 = wx.RadioButton(self, wx.ID_ANY, "", style=wx.RB_GROUP)
        self.radio_btn_5 = wx.RadioButton(self, wx.ID_ANY, "")
        self.radio_btn_1 = wx.RadioButton(self, wx.ID_ANY, "", style=wx.RB_GROUP)
        self.checkbox_3 = wx.CheckBox(self, wx.ID_ANY, "")
        self.checkbox_4 = wx.CheckBox(self, wx.ID_ANY, "")
        self.spin_ctrl_1 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=0, max=23, style=wx.SP_WRAP)
        self.spin_ctrl_7 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_4 = wx.Choice(self, wx.ID_ANY, choices=["AM", "PM"])
        self.slider_1 = wx.Slider(self, wx.ID_ANY, 0, 0, 1)
        self.radio_btn_2 = wx.RadioButton(self, wx.ID_ANY, "")
        self.button_4 = wx.ToggleButton(self, wx.ID_ANY, "Scan Now")
        self.progressbar = wx.Gauge(self, wx.ID_ANY, 100)
        self.choice_2 = wx.Choice(self, wx.ID_ANY, choices=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        self.spin_ctrl_3 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1, max=12, style=wx.SP_WRAP)
        self.spin_ctrl_4 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_5 = wx.Choice(self, wx.ID_ANY, choices=["AM", "PM"])
        self.radio_btn_3 = wx.RadioButton(self, wx.ID_ANY, "")
        self.checkbox_5 = wx.CheckBox(self, wx.ID_ANY, "")
        self.checkbox_6 = wx.CheckBox(self, wx.ID_ANY, "")
        self.choice_3 = wx.Choice(self, wx.ID_ANY, choices=["First Day", "Fortnightly", "Last Day"])
        self.spin_ctrl_5 = wx.SpinCtrl(self, wx.ID_ANY, "1", min=1, max=12, style=wx.SP_WRAP)
        self.spin_ctrl_6 = wx.SpinCtrl(self, wx.ID_ANY, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_6 = wx.Choice(self, wx.ID_ANY, choices=["AM", "PM"])
        self.button_5 = wx.Button(self, wx.ID_ANY, "Enable Real-time Moderation")
        self.hyperlink_1 = wx.adv.HyperlinkCtrl(self, wx.ID_ANY, "Got a feedback for us ?", "https://www.dtoxd.ai")
        self.button_3 = wx.Button(self, wx.ID_ANY, "OK")
        self.button_2 = wx.Button(self, wx.ID_ANY, "Cancel")
        self.button_1 = wx.Button(self, wx.ID_ANY, "Apply")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBUTTON, self.quick_deep_scan, self.radio_btn_4)
        self.Bind(wx.EVT_RADIOBUTTON, self.scan_daily_schedule, self.radio_btn_1)
        self.Bind(wx.EVT_RADIOBUTTON, self.scan_weekly_schedule, self.radio_btn_2)
        self.Bind(wx.EVT_TOGGLEBUTTON, self.scan_toggle, self.button_4)
        self.Bind(wx.EVT_RADIOBUTTON, self.scan_monthly_schedule, self.radio_btn_3)
        self.Bind(wx.EVT_CHECKBOX, self.realtime_processing, self.checkbox_5)
        self.Bind(wx.EVT_CHECKBOX, self.realtime_processing, self.checkbox_6)
        self.Bind(wx.EVT_BUTTON, self.apply_and_close, self.button_3)
        self.Bind(wx.EVT_BUTTON, self.quit, self.button_2)
        self.Bind(wx.EVT_BUTTON, self.apply_settings, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: _715811673__883977639__931769938_root_frame.__set_properties
        self.SetTitle("dtoxd : The Clean Digital Experience")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\g_host\\Desktop\\dtoxd_GUI\\src\\logo.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.SetFocus()
        self.frame_statusbar.SetStatusWidths([-1])

        # statusbar fields
        frame_statusbar_fields = ["lund_fakir"]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)
        self.radio_btn_4.SetValue(1)
        self.radio_btn_1.SetFocus()
        self.radio_btn_1.SetValue(1)
        self.spin_ctrl_1.SetMinSize((42, 20))
        self.spin_ctrl_7.SetMinSize((42, 20))
        self.choice_4.SetMinSize((44, 20))
        self.choice_4.SetSelection(0)
        self.slider_1.SetMinSize((65, 22))
        self.progressbar.SetMinSize((175, 25))
        self.progressbar.Hide()
        self.choice_2.SetMinSize((89, 22))
        self.choice_2.Enable(False)
        self.choice_2.SetSelection(0)
        self.spin_ctrl_3.SetMinSize((40, 22))
        self.spin_ctrl_3.Enable(False)
        self.spin_ctrl_4.SetMinSize((42, 22))
        self.spin_ctrl_4.Enable(False)
        self.choice_5.SetMinSize((44, 22))
        self.choice_5.Enable(False)
        self.choice_5.SetSelection(0)
        self.checkbox_5.Enable(False)
        self.checkbox_6.Enable(False)
        self.choice_3.SetMinSize((86, 22))
        self.choice_3.Enable(False)
        self.choice_3.SetSelection(0)
        self.spin_ctrl_5.SetMinSize((40, 22))
        self.spin_ctrl_5.Enable(False)
        self.spin_ctrl_6.SetMinSize((42, 22))
        self.spin_ctrl_6.Enable(False)
        self.choice_6.SetMinSize((44, 22))
        self.choice_6.Enable(False)
        self.choice_6.SetSelection(0)
        self.button_5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.button_5.Enable(False)
        self.hyperlink_1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: _715811673__883977639__931769938_root_frame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(9, 13, 0, 0)
        label_3 = wx.StaticText(self, wx.ID_ANY, "Content Scanner")
        label_3.SetForegroundColour(wx.Colour(0, 0, 0))
        label_3.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_3, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        static_line_1 = wx.StaticLine(self, wx.ID_ANY, style=wx.LI_VERTICAL)
        static_line_1.SetMinSize((4, 400))
        grid_sizer_1.Add(static_line_1, 0, wx.LEFT, 10)
        label_1 = wx.StaticText(self, wx.ID_ANY, "Schedule Scan")
        label_1.SetForegroundColour(wx.Colour(0, 0, 0))
        label_1.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_1, 0, wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP, 20)
        label_2 = wx.StaticText(self, wx.ID_ANY, "Quick Scan")
        label_2.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_2, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_5, 0, wx.LEFT | wx.TOP, 20)
        label_9 = wx.StaticText(self, wx.ID_ANY, "Deep Scan")
        grid_sizer_1.Add(label_9, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.TOP, 20)
        label_10 = wx.StaticText(self, wx.ID_ANY, "Daily")
        label_10.SetForegroundColour(wx.Colour(0, 0, 0))
        label_10.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_10, 0, wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_4 = wx.StaticText(self, wx.ID_ANY, "Images")
        label_4.SetForegroundColour(wx.Colour(0, 0, 0))
        label_4.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_5 = wx.StaticText(self, wx.ID_ANY, "Videos")
        label_5.SetForegroundColour(wx.Colour(0, 0, 0))
        label_5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.spin_ctrl_1, 0, wx.ALIGN_BOTTOM | wx.LEFT, 55)
        label_15 = wx.StaticText(self, wx.ID_ANY, ":")
        label_15.SetMinSize((3, 20))
        label_15.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_15, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT, 50)
        grid_sizer_1.Add(self.spin_ctrl_7, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT, 5)
        grid_sizer_1.Add(self.choice_4, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("C:\\Users\\g_host\\Desktop\\dtoxd_GUI\\src\\help-info.ico", wx.BITMAP_TYPE_ANY), style=wx.BORDER_NONE)
        grid_sizer_1.Add(bitmap_1, 0, wx.LEFT, 17)
        label_13 = wx.StaticText(self, wx.ID_ANY, "Sensitivity")
        label_13.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_13, 0, wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        label_17 = wx.StaticText(self, wx.ID_ANY, "Low")
        label_17.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_17, 0, wx.LEFT, 20)
        grid_sizer_1.Add(self.slider_1, 0, wx.ALIGN_RIGHT | wx.TOP, 0)
        label_18 = wx.StaticText(self, wx.ID_ANY, "High")
        label_18.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_18, 0, wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_2, 0, wx.ALIGN_BOTTOM | wx.LEFT, 0)
        label_11 = wx.StaticText(self, wx.ID_ANY, "Weekly")
        label_11.SetForegroundColour(wx.Colour(0, 0, 0))
        label_11.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_11, 0, wx.ALIGN_BOTTOM | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_4, 0, wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.progressbar, 0, wx.LEFT, 16)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.choice_2, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT, 30)
        grid_sizer_1.Add(self.spin_ctrl_3, 0, wx.ALIGN_BOTTOM | wx.LEFT, 50)
        label_14 = wx.StaticText(self, wx.ID_ANY, ":")
        label_14.SetMinSize((3, 20))
        label_14.SetForegroundColour(wx.Colour(0, 0, 0))
        grid_sizer_1.Add(label_14, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT, 35)
        grid_sizer_1.Add(self.spin_ctrl_4, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.choice_5, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 10)
        label_6 = wx.StaticText(self, wx.ID_ANY, "Real-time Content Moderation")
        label_6.SetForegroundColour(wx.Colour(0, 0, 0))
        label_6.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_3, 0, wx.ALIGN_BOTTOM | wx.LEFT, 0)
        label_12 = wx.StaticText(self, wx.ID_ANY, "Monthly")
        label_12.SetForegroundColour(wx.Colour(0, 0, 0))
        label_12.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_12, 0, wx.ALIGN_BOTTOM | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_7 = wx.StaticText(self, wx.ID_ANY, "Images")
        label_7.SetForegroundColour(wx.Colour(0, 0, 0))
        label_7.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_8 = wx.StaticText(self, wx.ID_ANY, "Videos")
        label_8.SetForegroundColour(wx.Colour(0, 0, 0))
        label_8.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_8, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.choice_3, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT, 30)
        grid_sizer_1.Add(self.spin_ctrl_5, 0, wx.ALIGN_BOTTOM | wx.LEFT, 50)
        label_16 = wx.StaticText(self, wx.ID_ANY, ":")
        label_16.SetMinSize((3, 20))
        label_16.SetForegroundColour(wx.Colour(0, 0, 0))
        grid_sizer_1.Add(label_16, 0, wx.ALIGN_BOTTOM | wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT, 35)
        grid_sizer_1.Add(self.spin_ctrl_6, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 10)
        grid_sizer_1.Add(self.choice_6, 0, wx.ALIGN_BOTTOM | wx.RIGHT, 10)
        grid_sizer_1.Add(self.button_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.hyperlink_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_3, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_2, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)
        sizer_1.Add(grid_sizer_1, 1, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        self.Centre()
        # end wxGlade

    def quit(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'quit' not implemented!")
        event.Skip()

    def documentation_help(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'documentation_help' not implemented!")
        event.Skip()

    def report_bugs(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'report_bugs' not implemented!")
        event.Skip()

    def check_for_updates(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'check_for_updates' not implemented!")
        event.Skip()

    def about_dtoxd(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'about_dtoxd' not implemented!")
        event.Skip()

    def quick_deep_scan(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'quick_deep_scan' not implemented!")
        event.Skip()

    def scan_daily_schedule(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'scan_daily_schedule' not implemented!")
        event.Skip()

    def scan_weekly_schedule(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'scan_weekly_schedule' not implemented!")
        event.Skip()

    def scan_toggle(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'scan_toggle' not implemented!")
        event.Skip()

    def scan_monthly_schedule(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'scan_monthly_schedule' not implemented!")
        event.Skip()

    def realtime_processing(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'realtime_processing' not implemented!")
        event.Skip()

    def apply_and_close(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'apply_and_close' not implemented!")
        event.Skip()

    def apply_settings(self, event):  # wxGlade: _715811673__883977639__931769938_root_frame.<event_handler>
        print("Event handler 'apply_settings' not implemented!")
        event.Skip()

# end of class _715811673__883977639__931769938_root_frame

class MyApp(wx.App):
    def OnInit(self):
        self.frame = _715811673__883977639__931769938_root_frame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

def hello():
    app=MyApp(0)
    app.MainLoop()
# if __name__ == "__main__":
#     app = MyApp(0)
#     app.MainLoop()