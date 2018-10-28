using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(myTest.Startup))]
namespace myTest
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
