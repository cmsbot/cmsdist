### RPM cms cmsmon-tools 0.3.10
## INITENV +PATH PYTHONPATH %i/${PYTHON_LIB_SITE_PACKAGES}
## NOCOMPILER

%define pkg CMSMonitoring
%define ver %realversion
%define cmsmon_commands nats-sub nats-pub nats-exitcodes-termui dbs_vm
Source0: https://github.com/dmwm/%pkg/archive/%ver.tar.gz

Requires: go

# RPM macros documentation
# http://www.rpm.org/max-rpm/s1-rpm-inside-macros.html
%prep
%setup -D -T -b 0 -n %pkg-%ver

%build
export GOCACHE=%{_builddir}/gocache
cd ..
cd %pkg-%ver
echo "build $PWD"
ls
mkdir -p gopath/bin
export GOPATH=$PWD/gopath
go get github.com/dmwm/cmsauth
go get github.com/vkuznet/x509proxy
go get github.com/sirupsen/logrus
go get github.com/prometheus/client_golang/prometheus
go get github.com/prometheus/common/log
go get github.com/prometheus/common/version
go get github.com/shirou/gopsutil/cpu
go get github.com/shirou/gopsutil/mem
go get github.com/shirou/gopsutil/load
go get github.com/shirou/gopsutil/process
go get github.com/go-stomp/stomp
go get github.com/nats-io/nats.go
go get github.com/gizak/termui/v3

# build monit tools
cd src/go/MONIT
go build monit.go
cd -
# build NATS tools
cd src/go/NATS
go build nats-sub.go
go build nats-pub.go
go build dbs_vm.go
go build nats-exitcodes-termui.go
cd -

%install
cd ../%pkg-%ver
echo "### current dir: $PWD"
cp src/go/MONIT/monit %i/
for cmd in %cmsmon_commands; do
if [ -f src/go/NATS/$cmd ]; then
cp src/go/NATS/$cmd %i/
fi
done

%post
for cmd in %cmsmon_commands; do
cp $RPM_INSTALL_PREFIX/%{pkgrel}/$cmd $RPM_INSTALL_PREFIX/common
done
