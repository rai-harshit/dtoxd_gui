#!/usr/bin/env python
# -*- coding: CP1252 -*-
#
# generated by wxGlade 0.9.3 on Wed May 29 14:30:27 2019
#

import wx
import wx.adv




class _715811673__883977639__931769938_root_frame(wx.Frame):
    def __init__(self, *args, **kwds):
        kwds["style"] = kwds.get("style", 0) | wx.BORDER_SIMPLE | wx.CAPTION | wx.CLIP_CHILDREN | wx.CLOSE_BOX | wx.MINIMIZE_BOX | wx.STAY_ON_TOP | wx.SYSTEM_MENU
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((720, 420))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.NewId(), "Quit", "Quit the application")
        self.Bind(wx.EVT_MENU, self.quit, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.NewId(), "Help", "Try documentation and tutorials")
        self.Bind(wx.EVT_MENU, self.documentation_help, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.NewId(), "Report Bugs", "Report bugs to Team dtoxd ")
        self.Bind(wx.EVT_MENU, self.report_bugs, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.NewId(), "Check for Updates", "Check for Updates")
        self.Bind(wx.EVT_MENU, self.check_for_updates, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.NewId(), "About dtoxd", "Learn more about dtoxd")
        self.Bind(wx.EVT_MENU, self.about_dtoxd, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, "About")
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.radio_btn_4 = wx.RadioButton(self, -1, "", style=wx.RB_GROUP)
        self.radio_btn_5 = wx.RadioButton(self, -1, "")
        self.radio_btn_1 = wx.RadioButton(self, -1, "", style=wx.RB_GROUP)
        self.checkbox_3 = wx.CheckBox(self, -1, "")
        self.checkbox_4 = wx.CheckBox(self, -1, "")
        self.spin_ctrl_1 = wx.SpinCtrl(self, -1, "1", min=0, max=23, style=wx.SP_WRAP)
        self.spin_ctrl_7 = wx.SpinCtrl(self, -1, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_4 = wx.Choice(self, -1, choices=["AM", "PM"])
        self.slider_1 = wx.Slider(self, -1, <new_properties._DefaultArgument object at 0x000001FFDE8F9D68>, 0, 10, style=wx.SL_AUTOTICKS | wx.SL_HORIZONTAL | wx.SL_MIN_MAX_LABELS)
        self.radio_btn_2 = wx.RadioButton(self, -1, "")
        self.button_4 = wx.ToggleButton(self, -1, "Scan Now")
        self.progressbar = wx.Gauge(self, -1, 100)
        self.choice_2 = wx.Choice(self, -1, choices=["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"])
        self.spin_ctrl_3 = wx.SpinCtrl(self, -1, "1", min=1, max=12, style=wx.SP_WRAP)
        self.spin_ctrl_4 = wx.SpinCtrl(self, -1, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_5 = wx.Choice(self, -1, choices=["AM", "PM"])
        self.radio_btn_3 = wx.RadioButton(self, -1, "")
        self.checkbox_5 = wx.CheckBox(self, -1, "")
        self.checkbox_6 = wx.CheckBox(self, -1, "")
        self.choice_3 = wx.Choice(self, -1, choices=["First Day", "Fortnightly", "Last Day"])
        self.spin_ctrl_5 = wx.SpinCtrl(self, -1, "1", min=1, max=12, style=wx.SP_WRAP)
        self.spin_ctrl_6 = wx.SpinCtrl(self, -1, "0", min=0, max=59, style=wx.SP_WRAP)
        self.choice_6 = wx.Choice(self, -1, choices=["AM", "PM"])
        self.button_5 = wx.Button(self, -1, "Enable Real-time Moderation")
        self.hyperlink_1 = wx.adv.HyperlinkCtrl(self, -1, "Got a feedback for us ?", "https://www.dtoxd.ai")
        self.button_3 = wx.Button(self, -1, "OK")
        self.button_2 = wx.Button(self, -1, "Cancel")
        self.button_1 = wx.Button(self, -1, "Apply")

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

    def __set_properties(self):
        self.SetTitle("dtoxd : The Clean Digital Experience")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("C:\\Users\\g_host\\Desktop\\dtoxd_GUI\\images\\logofinalfinal2_24x24.png", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.SetBackgroundColour(wx.Colour(240, 240, 240))
        self.SetFocus()
        self.radio_btn_4.SetValue(1)
        self.radio_btn_1.SetFocus()
        self.radio_btn_1.SetValue(1)
        self.spin_ctrl_1.SetMinSize((42, 20))
        self.spin_ctrl_7.SetMinSize((42, 20))
        self.choice_4.SetMinSize((44, 22))
        self.choice_4.SetSelection(0)
        self.progressbar.SetMinSize((175, 25))
        self.progressbar.Hide()
        self.choice_2.Enable(False)
        self.choice_2.SetSelection(0)
        self.spin_ctrl_3.SetMinSize((40, 20))
        self.spin_ctrl_3.Enable(False)
        self.spin_ctrl_4.SetMinSize((42, 20))
        self.spin_ctrl_4.Enable(False)
        self.choice_5.SetMinSize((44, 22))
        self.choice_5.Enable(False)
        self.choice_5.SetSelection(0)
        self.checkbox_5.Enable(False)
        self.checkbox_6.Enable(False)
        self.choice_3.Enable(False)
        self.choice_3.SetSelection(0)
        self.spin_ctrl_5.SetMinSize((40, 20))
        self.spin_ctrl_5.Enable(False)
        self.spin_ctrl_6.SetMinSize((42, 20))
        self.spin_ctrl_6.Enable(False)
        self.choice_6.SetMinSize((44, 22))
        self.choice_6.Enable(False)
        self.choice_6.SetSelection(0)
        self.button_5.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, ""))
        self.button_5.Enable(False)
        self.hyperlink_1.SetFont(wx.Font(10, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))

    def __do_layout(self):
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_1 = wx.GridSizer(9, 13, 0, 0)
        label_3 = wx.StaticText(self, -1, "Content Scanner")
        label_3.SetForegroundColour(wx.Colour(0, 0, 0))
        label_3.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_3, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        static_line_1 = wx.StaticLine(self, -1, style=wx.LI_VERTICAL)
        static_line_1.SetMinSize((4, 400))
        grid_sizer_1.Add(static_line_1, 0, wx.LEFT, 10)
        label_1 = wx.StaticText(self, -1, "Schedule Scan")
        label_1.SetForegroundColour(wx.Colour(0, 0, 0))
        label_1.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_1, 0, wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.TOP, 20)
        label_2 = wx.StaticText(self, -1, "Quick Scan")
        grid_sizer_1.Add(label_2, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_5, 0, wx.LEFT | wx.TOP, 20)
        label_9 = wx.StaticText(self, -1, "Deep Scan")
        grid_sizer_1.Add(label_9, 0, wx.LEFT | wx.TOP, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        label_10 = wx.StaticText(self, -1, "Daily")
        label_10.SetForegroundColour(wx.Colour(0, 0, 0))
        label_10.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_10, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_4 = wx.StaticText(self, -1, "Images")
        label_4.SetForegroundColour(wx.Colour(0, 0, 0))
        label_4.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        label_5 = wx.StaticText(self, -1, "Videos")
        label_5.SetForegroundColour(wx.Colour(0, 0, 0))
        label_5.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.spin_ctrl_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 55)
        label_15 = wx.StaticText(self, -1, ":")
        label_15.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        grid_sizer_1.Add(label_15, 0, wx.ALIGN_CENTER | wx.LEFT, 50)
        grid_sizer_1.Add(self.spin_ctrl_7, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
        grid_sizer_1.Add(self.choice_4, 0, wx.ALIGN_CENTER | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.slider_1, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_2, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        label_11 = wx.StaticText(self, -1, "Weekly")
        label_11.SetForegroundColour(wx.Colour(0, 0, 0))
        label_11.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_11, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.button_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.progressbar, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 16)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.choice_2, 0, wx.ALIGN_CENTER | wx.LEFT, 30)
        grid_sizer_1.Add(self.spin_ctrl_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 50)
        label_14 = wx.StaticText(self, -1, ":")
        label_14.SetForegroundColour(wx.Colour(0, 0, 0))
        grid_sizer_1.Add(label_14, 0, wx.ALIGN_CENTER | wx.LEFT, 35)
        grid_sizer_1.Add(self.spin_ctrl_4, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.choice_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        label_6 = wx.StaticText(self, -1, "Real-time Content Moderation")
        label_6.SetForegroundColour(wx.Colour(0, 0, 0))
        label_6.SetFont(wx.Font(13, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, 0, "Calibri"))
        grid_sizer_1.Add(label_6, 0, wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.radio_btn_3, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        label_12 = wx.StaticText(self, -1, "Monthly")
        label_12.SetForegroundColour(wx.Colour(0, 0, 0))
        label_12.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_12, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_5, 0, wx.LEFT, 20)
        label_7 = wx.StaticText(self, -1, "Images")
        label_7.SetForegroundColour(wx.Colour(0, 0, 0))
        label_7.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_7, 0, wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.checkbox_6, 0, wx.LEFT, 20)
        label_8 = wx.StaticText(self, -1, "Videos")
        label_8.SetForegroundColour(wx.Colour(0, 0, 0))
        label_8.SetFont(wx.Font(12, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Calibri"))
        grid_sizer_1.Add(label_8, 0, wx.LEFT, 20)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add((0, 0), 0, 0, 0)
        grid_sizer_1.Add(self.choice_3, 0, wx.ALIGN_CENTER | wx.LEFT, 30)
        grid_sizer_1.Add(self.spin_ctrl_5, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 50)
        label_16 = wx.StaticText(self, -1, ":")
        label_16.SetForegroundColour(wx.Colour(0, 0, 0))
        grid_sizer_1.Add(label_16, 0, wx.ALIGN_CENTER | wx.LEFT, 35)
        grid_sizer_1.Add(self.spin_ctrl_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.choice_6, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 10)
        grid_sizer_1.Add(self.button_5, 0, wx.LEFT, 20)
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
        grid_sizer_1.Add(self.hyperlink_1, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.LEFT, 20)
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

    def quit(self, event):
        print("Event handler 'quit' not implemented!")
        event.Skip()

    def documentation_help(self, event):
        print("Event handler 'documentation_help' not implemented!")
        event.Skip()

    def report_bugs(self, event):
        print("Event handler 'report_bugs' not implemented!")
        event.Skip()

    def check_for_updates(self, event):
        print("Event handler 'check_for_updates' not implemented!")
        event.Skip()

    def about_dtoxd(self, event):
        print("Event handler 'about_dtoxd' not implemented!")
        event.Skip()

    def quick_deep_scan(self, event):
        print("Event handler 'quick_deep_scan' not implemented!")
        event.Skip()

    def scan_daily_schedule(self, event):
        print("Event handler 'scan_daily_schedule' not implemented!")
        event.Skip()

    def scan_weekly_schedule(self, event):
        print("Event handler 'scan_weekly_schedule' not implemented!")
        event.Skip()

    def scan_toggle(self, event):
        print("Event handler 'scan_toggle' not implemented!")
        event.Skip()

    def scan_monthly_schedule(self, event):
        print("Event handler 'scan_monthly_schedule' not implemented!")
        event.Skip()

    def realtime_processing(self, event):
        print("Event handler 'realtime_processing' not implemented!")
        event.Skip()

    def apply_and_close(self, event):
        print("Event handler 'apply_and_close' not implemented!")
        event.Skip()

    def apply_settings(self, event):
        print("Event handler 'apply_settings' not implemented!")
        event.Skip()


class MyApp(wx.App):
    def OnInit(self):
        self.frame = _715811673__883977639__931769938_root_frame(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
