﻿///////////////////////////////////////////////////////////////////////////////
//
// This file was automatically generated by RANOREX.
// DO NOT MODIFY THIS FILE! It is regenerated by the designer.
// All your modifications will be lost!
// http://www.ranorex.com
//
///////////////////////////////////////////////////////////////////////////////

using System;
using System.Collections.Generic;
using System.Text;
using System.Text.RegularExpressions;
using System.Drawing;
using System.Threading;
using WinForms = System.Windows.Forms;

using Ranorex;
using Ranorex.Core;
using Ranorex.Core.Testing;
using Ranorex.Core.Repository;

namespace ZangConnectWebEx
{
#pragma warning disable 0436 //(CS0436) The type 'type' in 'assembly' conflicts with the imported type 'type2' in 'assembly'. Using the type defined in 'assembly'.
    /// <summary>
    ///The Hangouts recording.
    /// </summary>
    [TestModule("5a26c7c9-816c-4b9e-bfb2-f358f5a824e3", ModuleType.Recording, 1)]
    public partial class Hangouts : ITestModule
    {
        /// <summary>
        /// Holds an instance of the ZangConnectWebExRepository repository.
        /// </summary>
        public static ZangConnectWebExRepository repo = ZangConnectWebExRepository.Instance;

        static Hangouts instance = new Hangouts();

        /// <summary>
        /// Constructs a new instance.
        /// </summary>
        public Hangouts()
        {
        }

        /// <summary>
        /// Gets a static instance of this recording.
        /// </summary>
        public static Hangouts Instance
        {
            get { return instance; }
        }

#region Variables

#endregion

        /// <summary>
        /// Starts the replay of the static recording <see cref="Instance"/>.
        /// </summary>
        [System.CodeDom.Compiler.GeneratedCode("Ranorex", "7.2")]
        public static void Start()
        {
            TestModuleRunner.Run(Instance);
        }

        /// <summary>
        /// Performs the playback of actions in this recording.
        /// </summary>
        /// <remarks>You should not call this method directly, instead pass the module
        /// instance to the <see cref="TestModuleRunner.Run(ITestModule)"/> method
        /// that will in turn invoke this method.</remarks>
        [System.CodeDom.Compiler.GeneratedCode("Ranorex", "7.2")]
        void ITestModule.Run()
        {
            Mouse.DefaultMoveTime = 300;
            Keyboard.DefaultKeyPressTime = 100;
            Delay.SpeedFactor = 1.00;

            Init();

            Report.Log(ReportLevel.Info, "Website", "Opening web site 'https://mail.google.com/mail/u/0/#contacts' with browser 'chrome' in normal mode.", new RecordItemIndex(0));
            Host.Current.OpenBrowser("https://mail.google.com/mail/u/0/#contacts", "chrome", "", false, false, false, false, false);
            Delay.Milliseconds(0);
            
            Report.Log(ReportLevel.Info, "Delay", "Waiting for 15s.", new RecordItemIndex(1));
            Delay.Duration(15000, false);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=600,Y=600}.", new RecordItemIndex(2));
            Mouse.MoveTo(600, 600);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Move at {X=282,Y=379}.", new RecordItemIndex(3));
            Mouse.MoveTo(282, 379);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Delay", "Waiting for 2s.", new RecordItemIndex(4));
            Delay.Duration(2000, false);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=521,Y=534}.", new RecordItemIndex(5));
            Mouse.MoveTo(521, 534);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Delay", "Waiting for 15s.", new RecordItemIndex(6));
            Delay.Duration(15000, false);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=910,Y=483}.", new RecordItemIndex(7));
            Mouse.MoveTo(910, 483);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=784,Y=690}.", new RecordItemIndex(8));
            Mouse.MoveTo(784, 690);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Delay", "Waiting for 500ms.", new RecordItemIndex(9));
            Delay.Duration(500, false);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Move at {X=252,Y=199}.", new RecordItemIndex(10));
            Mouse.MoveTo(252, 199);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=252,Y=199}.", new RecordItemIndex(11));
            Mouse.MoveTo(252, 199);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Delay", "Waiting for 500ms.", new RecordItemIndex(12));
            Delay.Duration(500, false);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=1084,Y=220}.", new RecordItemIndex(13));
            Mouse.MoveTo(1084, 220);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Keyboard", "Key sequence '{Back}{NumPad4}'.", new RecordItemIndex(14));
            Keyboard.Press("{Back}{NumPad4}");
            Delay.Milliseconds(0);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=981,Y=361}.", new RecordItemIndex(15));
            Mouse.MoveTo(981, 361);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Keyboard", "Key sequence '1111a'.", new RecordItemIndex(16));
            Keyboard.Press("1111a");
            Delay.Milliseconds(0);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click at {X=978,Y=407}.", new RecordItemIndex(17));
            Mouse.MoveTo(978, 407);
            Mouse.Click(System.Windows.Forms.MouseButtons.Left);
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Delay", "Waiting for 10s.", new RecordItemIndex(18));
            Delay.Duration(10000, false);
            
            Report.Log(ReportLevel.Info, "Validation", "Validating AttributeEqual (Text='WebEx Meeting #114') on item 'CiscoWebExMeetingCenter.WebExMeetingHash111'.", repo.CiscoWebExMeetingCenter.WebExMeetingHash111Info, new RecordItemIndex(19));
            Validate.Attribute(repo.CiscoWebExMeetingCenter.WebExMeetingHash111Info, "Text", "WebEx Meeting #114");
            Delay.Milliseconds(100);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click item 'CiscoWebExMeetingCenter.EndMeeting' at 87;11.", repo.CiscoWebExMeetingCenter.EndMeetingInfo, new RecordItemIndex(20));
            repo.CiscoWebExMeetingCenter.EndMeeting.Click("87;11");
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click item 'EndMeeting.EndMeeting' at 132;16.", repo.EndMeeting.EndMeetingInfo, new RecordItemIndex(21));
            repo.EndMeeting.EndMeeting.Click("132;16");
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Keyboard", "Key sequence '{LWin 13}{LWin down}{Tab}'.", new RecordItemIndex(22));
            Keyboard.Press("{LWin 13}{LWin down}{Tab}");
            Delay.Milliseconds(0);
            
            Report.Log(ReportLevel.Info, "Keyboard", "Key sequence '{Tab}{LWin up}'.", new RecordItemIndex(23));
            Keyboard.Press("{Tab}{LWin up}");
            Delay.Milliseconds(0);
            
            Report.Log(ReportLevel.Info, "Mouse", "Mouse Left Click item 'GoogleHangoutsGoogleChrome.Close' at 22;9.", repo.GoogleHangoutsGoogleChrome.CloseInfo, new RecordItemIndex(24));
            repo.GoogleHangoutsGoogleChrome.Close.Click("22;9");
            Delay.Milliseconds(200);
            
            Report.Log(ReportLevel.Info, "Keyboard", "Key 'Ctrl+W' Press.", new RecordItemIndex(25));
            Keyboard.Press(System.Windows.Forms.Keys.W | System.Windows.Forms.Keys.Control, Keyboard.DefaultScanCode, Keyboard.DefaultKeyPressTime, 1, true);
            Delay.Milliseconds(0);
            
            Report.Log(ReportLevel.Info, "Keyboard", "Key 'Ctrl+W' Press.", new RecordItemIndex(26));
            Keyboard.Press(System.Windows.Forms.Keys.W | System.Windows.Forms.Keys.Control, Keyboard.DefaultScanCode, Keyboard.DefaultKeyPressTime, 1, true);
            Delay.Milliseconds(0);
            
        }

#region Image Feature Data
#endregion
    }
#pragma warning restore 0436
}
